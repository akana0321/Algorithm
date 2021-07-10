"""
    효율적인 화폐 구성
     - 입력 : n, m / n개의 줄에 각 화폐의 가치가 만들어짐
     - 출력 : m원을 만들기 위한 최소한의 화폐 개수, 불가능할 때는 -1을 출력
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
units = [0] * 101
for i in range(n):
    units[i] = int(stdin.readline())

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(units[i], m + 1):
        if d[j - units[i]] != 1001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - units[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

