"""
    치킨 배달
     - 입력 : N(2 <= N <= 50) M(1<= M <= 13)
             이후 N개의 줄에 도시의 정보가 주어짐(0은 빈칸, 1은 집, 2는 치킨집)
             집의 개수는 2N개를 넘지 않으며 적어도 1개는 존재, 치킨집의 개수는 M보다 크거나 같고 13보다는 작거나 같음
     - 출력 : 폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값
"""
from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
chicken, house = [], []

for r in range(n):
    city = list(map(int, stdin.readline().split()))
    for c in range(n):
        if city[c] == 1:
            house.append((r, c))  # 집
        elif city[c] == 2:
            chicken.append((r, c))  # 치킨집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합
candidates = list(combinations(chicken, m))
print(candidates)

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result


# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
