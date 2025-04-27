"""
    RGB 거리(https://www.acmicpc.net/problem/1149)
     - 입력 : 집의 수 N(2 <= N <= 1,000)
             이후 빨강 초록 파랑으로 칠하는 비용(<= 1,000)
     - 출력 : 모든 집을 칠하는 비용의 최솟값
"""
from sys import stdin

n = int(stdin.readline().strip())
cost = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
    cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1])

print(min(cost[n-1]))
