import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api.deps import get_db, get_current_user
from app.models.identity import User
from app.models.organization import OrganizationMember
from app.schemas.ai import AISearchRequest, AISearchResponse, AIEvidence
from app.ai.retrieval.engine import retrieval_engine
from app.ai.retrieval.context import context_builder
from app.ai.llm.client import llm_client
from app.ai.llm.prompts import build_system_prompt

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/search", response_model=AISearchResponse)
async def ai_search(
    request: AISearchRequest = Body(...),
    organization_id: uuid.UUID = Query(..., description="The organization context for the search"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Semantic AI search across indexed repositories.
    """
    # 1. Authorization: Ensure user is a member of the requested organization
    member = await db.scalar(
        select(OrganizationMember)
        .where(OrganizationMember.user_id == current_user.id, OrganizationMember.organization_id == organization_id)
    )
    if not member:
        raise HTTPException(status_code=403, detail="Not authorized to access this organization's data.")

    logger.info(f"User {current_user.id} initiated AI search in org {organization_id}")

    # 2. Retrieval
    try:
        raw_chunks = retrieval_engine.retrieve(
            query=request.query,
            organization_id=organization_id,
            repository_id=request.repository_id,
            limit=request.limit
        )
    except Exception as e:
        logger.error(f"Retrieval error: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve semantic context.")

    if not raw_chunks:
        return AISearchResponse(
            answer="No supporting code evidence found in the indexed repositories to answer your query.",
            evidence=[]
        )

    # 3. Context Construction
    try:
        context_chunks = await context_builder.build_context(db, raw_chunks)
        formatted_context = context_builder.format_for_llm(context_chunks)
    except Exception as e:
        logger.error(f"Context construction error: {e}")
        raise HTTPException(status_code=500, detail="Failed to construct context.")

    # 4. LLM Reasoning
    try:
        system_prompt = build_system_prompt(formatted_context)
        answer = await llm_client.generate_answer(system_prompt, request.query)
    except Exception as e:
        logger.error(f"LLM Reasoning error: {e}")
        raise HTTPException(status_code=502, detail="Failed to communicate with the reasoning engine.")

    # 5. Build Final Response
    evidence_list = []
    for chunk in context_chunks:
        evidence_list.append(
            AIEvidence(
                file_reference=chunk.file_reference,
                start_line=chunk.start_line,
                end_line=chunk.end_line,
                score=chunk.score,
                symbol_type=chunk.symbol_type
            )
        )

    return AISearchResponse(
        answer=answer,
        evidence=evidence_list
    )
