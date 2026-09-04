---
actor: type-extractor
task: EX-social-20261F_refine
target: corpus/EX-social-20261F/ (transcript.md, meta.yml, verify_log.tsv) + corpus/_images/EX-social-20261F/
status: done
updated: 260904
---

## 슬라이스 표

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 0 | 원본 실측 + 렌더(전 10쪽 dpi160) | done | corpus/_images/EX-social-20261F/p01~p10.png | PyMuPDF, sha256[:16]=72ca9763d3c18c15 bytes=7824451 확인 일치, page.rotation 전건 0(메타데이터로 회전 판정 불가 확인) |
| 1 | 회전·단 실측 + native/ 생성 | done | corpus/_images/EX-social-20261F/native/p01~p10.png(300dpi) | 임베드 이미지 전건 1개(4299x3035). 회전각이 PDF 홀/짝에 따라 정확히 교대(홀수=-90/짝수=+90). 정립 후 각 쪽은 물리 분할 없는 좌우 2열 인쇄 1장(EX-social-20261M과 다름 — 분할 불필요). p10은 자체 인쇄 내용 없음(bleed-through만, autocontrast로 재확인) |
| 2 | 표지(p01) + 문항1~10(p02~p04) 판독 | done | 판독 완료 | 전건 완결. 인쇄쪽 번호가 PDF 물리쪽 순서와 어긋남을 확인(p04=인쇄 3면) |
| 3 | 문항11~24(p05~p08) 판독 | done | 판독 완료 | 전건 완결. 절단·미발견 0건 |
| 4 | 단답형1~3(p08~p09) 판독 | done | 판독 완료 | 전건 완결. '수고하셨습니다' 종결 문구로 마지막 쪽 확인 |
| 5 | transcript.md/meta.yml/verify_log.tsv 작성 | done | corpus/EX-social-20261F/{transcript.md,meta.yml,verify_log.tsv} | 27문항 전건 완결, unreadable 행 0건. 배점 합계 100.0점 내부 정합 확인(수기 합산 + 자 재계산 일치) |
| 6 | S2 게이트 7축 실행 + 자체 결함 수정 | done | (verify_log.tsv 마지막 행에 기록) | 최초 실행 G2-a FAIL(중복 배점 대괄호 + 임의 소제목이 자의 TO_SOD 상태전이를 조기 발화) → 두 결함 모두 본 전사자의 문서 실수로 확인, 자 코드 무수정 확인 후 문서만 수정 → 재실행 전건 통과. F1-2(원본 정상인데 걸리면 결정요청) 해당 없음 — 최종적으로 EX-social-20261F는 GATE3 FAIL 줄에 없음 |

NEXT: (없음 — 유닛 완료, F1/F3 시연자 요건 충족) 메인 루프가 이 결과(7축 전건 통과)를 근거로
판정 `output/260903/rev/260903_06_arbiter_ruling_cycle1_f.md` F3-1에 따라 나머지 8유닛(F3-2 사전
여백 실측 포함) 발주를 재판정 없이 진행할 수 있다. type-proposer는 corpus/EX-social-20261F/transcript.md를
열어 S3 분류에 진입 가능(1차 정제 게이트 충족).
