"""
    볼링공 고르기
     - 입력 : 볼링공의 개수 N(1 <= N <= 1,000), 공의 최대 무게 M(1 <= M <= 10)
             각 볼링공의 무게 K가 공백으로 구분대어 주어짐(1 <= K <= M)
     - 출력 : 두 사람이 볼링공을 고르는 경우의 수
"""
from sys import stdin
n, m = map(int, stdin.readline().split())
balls = list(map(int, stdin.readline().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for ball in balls:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[ball] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)