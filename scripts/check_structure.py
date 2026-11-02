from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
files=[root/'AGENTS.md',root/'.agents/skills/academic-peer-review-revision/SKILL.md']
for f in files:
    if not f.exists():
        sys.exit(f'MISSING: {f}')
s=files[1].read_text()
if not s.startswith('---\n') or '\nname:' not in s or '\ndescription:' not in s:
    sys.exit('Invalid SKILL frontmatter')
print('PASS: AGENTS.md and skill structure present')