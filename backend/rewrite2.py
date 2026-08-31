import uuid
import re

with open('app/api/v1/endpoints/organization_bugs.py', 'r') as f:
    bugs_content = f.read()

bugs_content = bugs_content.replace('organization_id=organization_id,\n            organization_id=organization_id,', 'organization_id=organization_id,')

with open('app/api/v1/endpoints/organization_bugs.py', 'w') as f:
    f.write(bugs_content)
