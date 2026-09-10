"""Current author-side comparison; revision3 artifacts stay historical."""
import importlib.util
from pathlib import Path

path = Path(__file__).with_name('260910_info_revision3_review.py')
spec = importlib.util.spec_from_file_location('review', path)
review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)
updates = '''A/8|A25; B9|所有 행 상대 순위와 동점 위치 우선순위를 구한다. 단일 최적 행 선택 A25와 달리 모든 행을 순위화한다. B9는 순차 문자 일치로 탐색 상태를 전진시킨다.
A/9|기출 단답7; B9|인덱스 순서로 중복 없는 쌍을 만들고 자료값의 차이를 판정한다. B9는 가능한 모든 쌍을 세지 않고 다음 필요 문자만 순서대로 고른다.
A/12|기존26-19; B16|임시 변수로 이전 상태를 보존해 두 상태를 교차 전달한다. B16은 아래쪽 두 후보의 최적 집계값을 위로 전달한다.
A/16|개념 p08 Quiz6; B2|대각선에서 읽은 값으로 다른 열을 갱신한다. B2는 순환 이동으로 정한 도착 칸의 횟수를 집계한다.
A/17|기존26-3; B2|조건별 가감 채점을 제거했다. 출발·도착 상태가 이차원 계수 위치를 결정한다. B2의 단일 도착 빈도와 달리 두 상태의 방향 관계를 보존한다.
A/21|개념 p09 Quiz9; B3|전역/지역 추적 대신 다음 필요 값이 성공 때마다 바뀌는 누락 탐색이다. 중복은 건너뛰며 빈틈에서 조기 반환한다. B3의 고정 임계값 첫 일치와 다르다.
A/23|기존26-20; B23|누적을 계속하며 최초 통과 회차만 보존한다. B23은 실패 때 초기화되는 현재 연속 길이와 최장 기록을 나누어 추적한다.
B/2|기출 단답2; A14|대칭 위치 합산을 제거했다. 출발 위치별 순환 도착 칸에 횟수를 모은다. A14는 하나의 위치 상태를 누적해 문자를 고른다.
B/3|개념 p09 Quiz9; A21|고정 조건을 처음 만족하면 조기 반환하며 없으면 별도 값을 반환한다. A21은 성공할 때마다 탐색 목표가 바뀐다.
B/9|기존26-21; B3|곱집합의 일치 쌍 세기를 제거했다. 필요 문자를 찾을 때만 목표 위치를 전진시켜 부분수열 위치를 만든다. 한번의 첫 반환 B3과 다르다.
B/15|개념 p08 Quiz8; B19|독립 함수 반환값 합산을 제거했다. 가운데 비교로 후보 구간 전체를 줄이며 발견/구간 역전을 판정한다. B19는 한 원소씩 축소하는 재귀 상대 위치 보정이다.
B/16|개념 p08 Quiz7; A25|행 사이 단순 교차 누적을 제거했다. 아래부터 두 후보의 최적 누적값을 선택해 위로 전달한다. A25는 서로 독립인 행을 평가해 하나를 고른다.
B/21|기존26-14; A4|전역 읽기 비교를 제거했다. 검사용 마지막 칸과 자료 구간을 분리하고 함수 검사의 실패 행만 복구해 이력을 남긴다. A4는 조건을 통과한 행의 범위 누적이다.'''
new = {line.split('|',1)[0]: line for line in updates.splitlines()}
new['A/8'] = new['A/8'].replace('所有', '모든')
review.NOTES = '\n'.join(new.get(line.split('|',1)[0], line) for line in review.NOTES.splitlines())
if __name__ == '__main__':
    review.main('4')
