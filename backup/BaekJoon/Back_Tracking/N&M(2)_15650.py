"""
    N과 M(2) (https://www.acmicpc.net/problem/15650)
     - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
     - 입력 : N M (1 <= M <= N <= 8)
     - 출력 : 한 줄에 하나 씩 출력
                중복 X, 각 수열은 공백으로 구분해서 출력
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
check = [False] * n
result = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join([str(x) for x in result]))
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        result.append(i+1)
        dfs(depth+1, n, m)
        result.pop()
        for j in range(i+1, n):
            check[j] = False


dfs(0, n, m)

"""
itertools로 풀기

from itertools import combinations

N, M = map(int, input().split())
C = combinations(range(1, N+1), M)  # iter(tuple)
for i in C:
    print(' '.join(map(str, i)))  # tuple -> str
"""
