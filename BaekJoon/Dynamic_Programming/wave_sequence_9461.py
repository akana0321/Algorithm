"""
    파도반 수열(https://www.acmicpc.net/problem/9461)
     - 입력 : 테스트 케이스의 개수 T
             이후 N(1 <= N <= 100)
     - 출력 : 각 테스트 케이스마다 P(N) 출력
"""
from sys import stdin

t = int(stdin.readline().strip())
n = [int(stdin.readline().strip()) for _ in range(t)]

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

for i in range(6, max(n) + 1):
    dp[i] = dp[i-1] + dp[i-5]

for i in n:
    print(dp[i])
