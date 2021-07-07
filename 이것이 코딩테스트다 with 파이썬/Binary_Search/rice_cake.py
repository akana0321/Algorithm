"""
    떡볶이 떡 만들기
     - 입력 : 떡의 개수 n, 요청한 떡의 길이 m / 개별 떡의 높이가 공백으로 구분되어 입력
     - 출력 : 최소 m 만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값

    * 전형적인 이진 탐색 문제이자, 파라메트릭 서치(Parametric Search) 유형의 문제
      파라메트릭 서치는 최적화 문제를 결정 문제(yes or no)로 해결하는 기법
      '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 사용
      이진 탐색으로 범위를 좁히기
    * 시작점은 0, 끝점은 가장 긴 떡의 길이로 시작. 중간점으로 잘랐을 때 절단된 떡의 합을 더하여
      목표값보다 길면 시작점을 중간점 + 1, 짧으면 끝점을 중간점 - 1 한다
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
riceCakes = list(map(int, stdin.readline().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(riceCakes)

# 이진 탐색 수행(반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for riceCake in riceCakes:
        # 잘랐을 때 덕의 양 계산
        if riceCake > mid:
            total += riceCake - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 많다면 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)