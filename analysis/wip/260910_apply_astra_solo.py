"""Apply the explicit user model policy without modifying the difficulty ruler."""
from pathlib import Path
import sys
import json
import hashlib

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from textpatch import patch

marker = '## 260910 사용자 우선 지침: Astra 단독 운영'
block = '\n\n' + marker + '''

현재 모델/팀 운영은 `docs/ASTRA_EXECUTION_POLICY.md`를 우선 적용한다.
`gpt-6-astra` 단독 실행; 기존 팀 발주·재개 중단; 검토·감사·맹목 풀이·최종 판정은 Astra 전용이며 Sol 참여 금지.
Astra 팀장 + Sol 비감사 보조는 성능 부족 실측 후 사용자 결정으로만 검토 가능한 미승인 대안이다.
이전 팀 필수·Sol 배정·외부 Opus 필수 서술은 현재 실행의 선행조건이 아니다.
자기검산을 독립 감사로 표시하지 않으며 독립 단계는 깨끗한 Astra 컨텍스트에서 순차 수행한다.
배포 증거·작성/감사 분리·append-only·two-key는 유지한다. 모델 지침 개정은 배포 승인이 아니다.
'''
paths = ['AGENTS.md', 'CLAUDE.md', 'analysis/REV_GUIDE.md', 'README.md',
         'docs/CODEX_TEAM_ASSURANCE_GUIDE.md', 'docs/OPUS_ASSURANCE_TEAM.md']
paths += [str(p.relative_to(ROOT)).replace('\\', '/') for p in sorted((ROOT / '.claude/agents').glob('*.md'))]
edits = []
for rel in paths:
    path = ROOT / rel
    old = path.read_text(encoding='utf-8-sig')
    if marker not in old:
        edits.append((path, old, old.rstrip() + block))
check = ROOT / 'tools/check_assurance_contract.py'
old = check.read_text(encoding='utf-8')
anchor = '\nROLE_FILES = ['
addition = '''
# Current operational policy; legacy Sol TOMLs below are archival schema checks,
# not permission to dispatch them for review/audit.
for policy_target in ("AGENTS.md", "CLAUDE.md", "analysis/REV_GUIDE.md", "README.md"):
    TEXT_REQUIREMENTS[policy_target] = TEXT_REQUIREMENTS.get(policy_target, []) + [
        "docs/ASTRA_EXECUTION_POLICY.md", "Astra 전용이며 Sol 참여 금지"
    ]
TEXT_REQUIREMENTS["docs/ASTRA_EXECUTION_POLICY.md"] = [
    "gpt-6-astra", "현재 미승인", "자기검산", "two-key", "전수 ID"
]
for policy_role in sorted((ROOT / ".claude/agents").glob("*.md")):
    relative_role = policy_role.relative_to(ROOT).as_posix()
    TEXT_REQUIREMENTS[relative_role] = TEXT_REQUIREMENTS.get(relative_role, []) + [
        "docs/ASTRA_EXECUTION_POLICY.md", "Astra 전용이며 Sol 참여 금지"
    ]
'''
if '# Current operational policy;' not in old:
    assert old.count(anchor) == 1
    edits.append((check, old, old.replace(anchor, '\n' + addition + anchor)))
for path, old, new in edits:
    patch(path, [(old, new)], dry_run=True)
for path, old, new in edits:
    patch(path, [(old, new)])
record = {'executor': 'Codex/OMX main loop', 'actual_model': 'unexposed',
          'release': 'BLOCKED', 'changes': []}
for path, _, _ in edits:
    b = path.read_bytes()
    record['changes'].append({'path': path.relative_to(ROOT).as_posix(), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})
(ROOT / 'output/260910/rev/260910_12_astra_solo_policy.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('policy files updated:', len(edits))
