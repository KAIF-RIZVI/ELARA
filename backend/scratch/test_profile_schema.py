from app.schemas.profile import DeveloperProfileResponse
from app.models.developer import DeveloperProfile
import uuid

profile = DeveloperProfile(
    id=uuid.uuid4(),
    user_id=uuid.uuid4(),
)

try:
    resp = DeveloperProfileResponse.model_validate(profile)
    print("SUCCESS")
except Exception as e:
    print("FAILED")
    print(e)
