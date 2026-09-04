---
actor: type-extractor
task: EX-social-20261M_R
target: corpus/EX-social-20261M/{transcript.md,meta.yml,verify_log.tsv} + corpus/_images/EX-social-20261M/native/
status: done
updated: 260904
---

## 슬라이스 표

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 0 | PRD·판정 재확인 | done | (읽기만) | output/260903/260903_01_cycle1_prd.md §3 「스캔 원본 렌더 규격」·「S1-R」, 판정 260903_04(A1~A4 approve)·260903_05(E1-1·E3-1) 확인 |
| 1 | 임베드 이미지 실측 + 회전각 결정(8쪽 전건) | done | (판정 근거) | 페이지당 이미지 1개(2150x3035 jpeg) 확인, dpi=300(계산 299.5356->round). p01~p08 각각 -90/+90 rotate 시험 후 육안 확인으로 홀수쪽=-90/짝수쪽=+90 확정 |
| 2 | native 렌더 스크립트 실행 | done | corpus/_images/EX-social-20261M/native/p01.png, p02_L/R.png ~ p08_L/R.png (OV=180, 거터 w//2=1517, 실측범위 1467~1576) | 기존 pNN.png 8장 무수정 확인(파일 미변경) |
| 3 | p01~p08 L/R 재판독(문항 1~15) | done | transcript.md §S1-R 표 일부 | 1,3,4,5,7,9,10,11,13,14,15 재확인 — 12는 신규 구조 정보(용어 미확정) |
| 4 | p06~p08 L/R 재판독(문항 16~24, 단답형1~3) | done | transcript.md §S1-R 표 나머지 | 16,18,21,23,단답형3 미발견 재확인, 22 선택지④ 완결 신규 확인, 24·단답형1·2 절단 지점 동일 재확인 |
| 5 | 6,8 재확인(여백 없음 근거) | done | transcript.md §S1-R 표 | p03 좌/우단이 각각 5,7번 서술로 이미 하단까지 채워짐을 근거로 명시 |
| 6 | 정식 문항 머리 보강(### 25~27 + `## 단답형` 전환줄) | done | transcript.md §S1-R 말미 | C-A3-1·E1-1 충족. item_heads 24->27 |
| 7 | verify_log.tsv corrected 17행 append | done | corpus/EX-social-20261M/verify_log.tsv (27->44행) | 기존 27행 무수정 확인(diff 없음), meta.yml 필드 변경 2건도 로그 |
| 8 | meta.yml method/confidence 주석 갱신 | done | corpus/EX-social-20261M/meta.yml | old->new verify_log 로그 완료 |
| 9 | typeid_hits/bracket-score 오탐 검사 | done | (검사만) | grep으로 PFX-NN 0건, 신규 절 내 대괄호+점수 패턴 0건(기존 15건은 원본 절, 무수정) 확인 |
| 10 | S2 게이트 7축 실행 | done | (return값 참조) | 실측: pages=8 unit_files=3 typeid_hits=0 present=3 empty=0 item_heads=27 declared_items=27 (6축 PASS). G2-a는 `[FAIL] GATE 3 mismatches=1 -- EX-social-20261M`(declared n=24 extracted n=15) — PRD 기대치(24/24)에 못 미침. 9개 선택형 문항(2,6,8,12,14,16,18,21,23)의 배점이 native 300dpi 재판독으로도 8쪽 안에 실재하지 않음을 재확인했으므로 자를 통과시키려 배점을 지어내지 않았다(원칙 12-a·9-c-iii) |
| 11 | doc.page_count 재확인(9쪽 존재 가능성 배제) | done | (검사만) | `fitz.open(...).page_count` = 8, 원본 PDF 자체가 8쪽뿐임을 재확인 — 누락 문항이 안 보이는 페이지에 있는 것이 아님 |

NEXT: (없음 — 이 유닛 재정제 완료) 메인 루프가 이 사실(G2-a 미충족, 9개 선택형 문항 배점 실재하지 않음)을 그대로 사용자·판정 라인에 전달한다. type-proposer는 여전히 이 transcript.md(§0~§S1-R)를 열어 진행 가능(분류 대상은 확인된 부분판독/완결 문항).
