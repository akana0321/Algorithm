"""
    01타일(https://www.acmicpc.net/problem/1904)
     - 1 하나만으로 이루어진 타일 또는 00 타일만 이용할 수 있음
     - 입력 : 자연수 N (1 <= N <= 1,000,000)
     - 출력 : 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지 출력
"""
from sys import stdin

n = int(stdin.readline().strip())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
