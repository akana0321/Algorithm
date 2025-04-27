"""
    개미 전사
     - 입력 : 식량 창고의 개수 / 저장된 식량들
     - 출력 : 최댓값
"""
from sys import stdin

n = int(stdin.readline().strip())
store = list(map(int, stdin.readline().split()))

d = [0] * 100

d[0] = store[0]
d[1] = max(store[0], store[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + store[i])

print(d[n - 1])