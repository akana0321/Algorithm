"""
    ATM(https://www.acmicpc.net/problem/11399)
     - 입력 : 사람의 수 N(1 <= N <= 1,000)
             각 사람이 돈을 인출하는데 걸리는 시간 Pi(1 <= Pi <= 1,000)
"""
from sys import stdin

n = int(stdin.readline().strip())
info = list(map(int, stdin.readline().split()))
info.sort(reverse=True)
result = 0

for i in range(1, n + 1):
    result += info[i - 1] * i

print(result)