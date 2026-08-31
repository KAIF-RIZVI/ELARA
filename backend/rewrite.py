import uuid
import re

with open('app/api/v1/endpoints/bugs.py', 'r') as f:
    bugs_content = f.read()

# Fix bugs.py to remove get_org_id_for_workspace
bugs_content = re.sub(r'async def get_org_id_for_workspace.*?(?=@router.post)', '', bugs_content, flags=re.DOTALL)
bugs_content = re.sub(r'organization_id = await get_org_id_for_workspace\(db, workspace_id\)\s+', '', bugs_content)
bugs_content = re.sub(r'organization_id=organization_id,', '', bugs_content)

with open('app/api/v1/endpoints/bugs.py', 'w') as f:
    f.write(bugs_content)

