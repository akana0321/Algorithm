"""
    블랙잭(https://www.acmicpc.net/problem/2798)
     - 입력 : 카드의 개수 N (3 <= N <= 100) 목표값 M(10 <= M <= 300,000)
             이후 N개의 카드(<= 100,000, 양의 정수)
     - 출력 : M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력
"""
from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))

selections = combinations(cards, 3)
selections_sum = []

for selection in selections:
    selections_sum.append(sum(selection))

selections_sum = list(set(selections_sum))
result = 0

for ele in selections_sum:
    if (m - result) >= (m - ele) >= 0:
        result = ele

print(result)