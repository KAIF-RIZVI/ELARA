from fastapi import APIRouter
from app.api.deps import CurrentUser

router = APIRouter()

@router.get("/me")
async def get_current_user(current_user: CurrentUser):
    """
    Get the currently authenticated user's details.
    """
    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_active": current_user.is_active,
        "is_superuser": current_user.is_superuser
    }
