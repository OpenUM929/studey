from pathlib import Path
import sys
sys.path.insert(0, 'tools')
from textpatch import patch, append_row
w = 'analysis/wip/mainloop_260907_math2_revision_release.md'
t = Path(w).read_text(encoding='utf-8')
anchor = next(x for x in t.splitlines() if x.startswith('NEXT:'))
note = ('## 260908 사용자 요청 범위 분기\n\n'
        '32제 감사 요청으로 기존 25·40제 NEXT를 보존한 채 별도 구조·계보 점검을 수행했다. '
        '32u는 후속 별도 세트라는 기록이 있어 삭제하지 않았다. '
        '증거·해시·검증 명령: output/260908/rev/260908_01_math2_32_pre_audit.md 및 inventory.json. '
        '원본2개 무변경; 새 보고 소유자 Codex/OMX. 외부 감사 미실행. '
        '32제 NEXT: 외부 A1 pilot 예산 실측 후 진행, 로컬 WIP 회신 확인. '
        '25·40제의 output/260907/rev/260907_03_opus_audit_reply.md 존재는 발견했으나 이번 범위에서 반영하지 않았다.\n\n')
if note not in t:
    patch(w, [(anchor, note + anchor)])
row = '| 260908 | [32제·32u 감사 착수](../output/260908/rev/260908_01_math2_32_pre_audit.md) | Codex/OMX proposal: 각32문항 답행 집합 일치; 32u 후속 세트 기록 및 ID 오류; 원본 무변경·삭제 없음·외부 수학감사 미실행 | 검토필요 | output/260830/260830_01_math2_graded_new_forms_32.md · output/260830/260830_02_math2_unused_axes_32.md |'
if row not in Path('analysis/REV_LOG.md').read_text(encoding='utf-8'):
    append_row('analysis/REV_LOG.md', row)
print('SCOPE_RECORDED')
