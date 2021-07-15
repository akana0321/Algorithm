"""
    만들 수 없는 금액
     - 입력 : 동전의 개수 N(1 <= N <= 1,000) / 각 동전의 화폐 단위(<= 1,000,000)
     - 출력 : 만들 수 없는 금액의 최솟값
"""
from sys import stdin

n = int(stdin.readline().strip())
coins = list(map(int, stdin.readline().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)