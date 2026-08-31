from typing import Any
from fastapi import APIRouter, Depends, Header, Request, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
import uuid
import hashlib
import json

from app.api import deps
from app.schemas.bug import BugIntakeCreate, BugResponse, BugCreate
from app.services.bug import bug_service
from app.models.identity import APIKey
from app.models.bug import BugSource, Bug
from app.core.rate_limit import limiter
from sqlalchemy import select
from app.models.bug import IdempotencyKey

router = APIRouter()

@router.post(
    "/bugs",
    response_model=BugResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a Bug via External Intake",
    description="Intake a bug securely from an external application using a Workspace API Key."
)
@limiter.limit("20/minute")
async def create_bug_intake(
    request: Request,
    bug_in: BugIntakeCreate,
    db: AsyncSession = Depends(deps.get_db),
    api_key: APIKey = Depends(deps.verify_api_key),
    idempotency_key: str | None = Header(None, alias="Idempotency-Key")
) -> Any:
    # Validate Idempotency-Key length if provided
    if idempotency_key and len(idempotency_key) > 255:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Idempotency-Key header too long"
        )

    bug_payload = bug_in.model_dump()
    
    # Hash the payload to verify payload matching for idempotency
    payload_str = json.dumps(bug_payload, sort_keys=True, default=str)
    request_hash = hashlib.sha256(payload_str.encode()).hexdigest()
    
    org_id = api_key.organization_id
    ws_id = api_key.workspace_id
    
    if idempotency_key:
        import struct
        from sqlalchemy import func
        # 1. Acquire transaction-level advisory lock based on workspace/org + key hash
        # This guarantees concurrent identical requests are serialized strictly
        lock_seed = str(ws_id) if ws_id else str(org_id)
        lock_hash = hashlib.sha256((lock_seed + idempotency_key).encode()).digest()
        lock_id = struct.unpack("q", lock_hash[:8])[0]
        
        await db.execute(select(func.pg_advisory_xact_lock(lock_id)))
        
        # 2. Check if the key already exists
        result = await db.execute(
            select(IdempotencyKey).where(
                IdempotencyKey.organization_id.is_not_distinct_from(org_id),
                IdempotencyKey.workspace_id.is_not_distinct_from(ws_id),
                IdempotencyKey.key == idempotency_key
            )
        )
        existing_key = result.scalar_one_or_none()
        
        if existing_key:
            if existing_key.request_hash != request_hash:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Idempotency key already used with different payload"
                )
            
            # Fetch the original bug to return
            bug_result = await db.execute(select(Bug).where(Bug.id == existing_key.bug_id))
            existing_bug = bug_result.scalar_one_or_none()
            if not existing_bug:
                raise HTTPException(status_code=500, detail="Original bug not found")
                
            from fastapi.responses import JSONResponse
            from fastapi.encoders import jsonable_encoder
            return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(existing_bug))
            
        # We create the bug, strictly binding it to the workspace and organization of the API key
        # We pass commit=False so our transaction (and xact_lock) remains active!
        created_bug = await bug_service.create_bug(
            db=db,
            obj_in=BugCreate(**bug_payload),
            organization_id=org_id,
            workspace_id=ws_id,
            source=BugSource.API,
            commit=False
        )
        
        # 3. Insert IdempotencyKey AFTER bug is created, so we have the real bug_id
        new_idempotency_record = IdempotencyKey(
            organization_id=org_id,
            workspace_id=ws_id,
            key=idempotency_key,
            request_hash=request_hash,
            bug_id=created_bug.id
        )
        db.add(new_idempotency_record)
        
        # Commit the transaction (this commits both the Bug and the IdempotencyKey, and releases xact_lock!)
        await db.commit()
        await db.refresh(created_bug)
        return created_bug

    # If no idempotency key is provided, just create the bug normally
    created_bug = await bug_service.create_bug(
        db=db,
        obj_in=BugCreate(**bug_payload),
        organization_id=org_id,
        workspace_id=ws_id,
        source=BugSource.API,
        commit=True
    )
    
    return created_bug
