from fastapi import APIRouter, Depends, HTTPException, status
from typing import Any
from app.api.deps import SessionDep, CurrentUser
from app.schemas.profile import DeveloperProfileCreate, DeveloperProfileUpdate, DeveloperProfileResponse
from app.services.profile import profile_service

router = APIRouter()

@router.get("/me", response_model=DeveloperProfileResponse)
async def get_my_profile(db: SessionDep, current_user: CurrentUser):
    """
    Get the currently authenticated user's developer profile.
    """
    profile = await profile_service.get_by_user(db, user_id=current_user.id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Developer profile not found"
        )
    return profile

@router.post("/me", response_model=DeveloperProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_my_profile(
    *,
    db: SessionDep,
    current_user: CurrentUser,
    profile_in: DeveloperProfileCreate
):
    """
    Create a developer profile for the currently authenticated user.
    """
    try:
        profile = await profile_service.create_profile(
            db, user_id=current_user.id, obj_in=profile_in.model_dump(exclude_unset=True)
        )
        return profile
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.patch("/me", response_model=DeveloperProfileResponse)
async def update_my_profile(
    *,
    db: SessionDep,
    current_user: CurrentUser,
    profile_in: DeveloperProfileUpdate
):
    """
    Update the developer profile for the currently authenticated user.
    """
    profile = await profile_service.update_profile(
        db, user_id=current_user.id, obj_in=profile_in.model_dump(exclude_unset=True)
    )
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Developer profile not found"
        )
    return profile
