import uuid
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_service import BaseService
from app.models.developer import DeveloperProfile
from app.repositories.profile import RepositoryDeveloperProfile, profile_repo

class ProfileService(BaseService[DeveloperProfile, RepositoryDeveloperProfile]):
    
    def _calculate_completion(self, profile: DeveloperProfile) -> int:
        """Calculate the profile completion percentage based on filled fields."""
        fields_to_check = [
            profile.first_name,
            profile.last_name,
            profile.display_name,
            profile.bio,
            profile.company,
            profile.designation,
            profile.primary_role,
            profile.experience_years,
            profile.location,
            profile.primary_language,
            profile.github_username,
            profile.linkedin_url,
            profile.tech_stack,
            profile.frameworks,
            profile.databases,
            profile.cloud_platforms,
            profile.skills,
            profile.areas_of_expertise
        ]
        
        filled_count = 0
        for f in fields_to_check:
            if f is None:
                continue
            if isinstance(f, (dict, list)) and len(f) == 0:
                continue
            if isinstance(f, str) and f.strip() == "":
                continue
            filled_count += 1
            
        total_fields = len(fields_to_check)
        
        return int((filled_count / total_fields) * 100)

    async def get_by_user(self, db: AsyncSession, user_id: uuid.UUID) -> DeveloperProfile | None:
        return await self.repository.get_by_user_id(db, user_id)

    async def create_profile(
        self, db: AsyncSession, user_id: uuid.UUID, obj_in: dict[str, Any]
    ) -> DeveloperProfile:
        existing = await self.get_by_user(db, user_id)
        if existing:
            raise ValueError("Profile already exists for this user")
            
        obj_in["user_id"] = user_id
        
        # We manually instantiate to calculate completion before inserting
        profile = DeveloperProfile(**obj_in)
        profile.profile_completion_percentage = self._calculate_completion(profile)
        
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
        return profile

    async def update_profile(
        self, db: AsyncSession, user_id: uuid.UUID, obj_in: dict[str, Any]
    ) -> DeveloperProfile | None:
        profile = await self.get_by_user(db, user_id)
        if not profile:
            return None
            
        for field, value in obj_in.items():
            if hasattr(profile, field):
                setattr(profile, field, value)
                
        profile.profile_completion_percentage = self._calculate_completion(profile)
        
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
        return profile

profile_service = ProfileService(repository=profile_repo)