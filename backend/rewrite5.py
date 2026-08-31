with open('app/api/v1/endpoints/organization_bugs.py', 'r') as f:
    content = f.read()

import re
content = re.sub(r'organization_id=organization_id,\s*organization_id=organization_id', 'organization_id=organization_id', content)

with open('app/api/v1/endpoints/organization_bugs.py', 'w') as f:
    f.write(content)
