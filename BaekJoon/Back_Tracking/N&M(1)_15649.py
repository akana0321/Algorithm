"""
    N과 M(1) (https://www.acmicpc.net/problem/15649)
     - 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
     - 입력 : N M(1 <= M <= N <= 8)
     - 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열
                중복되는 수열 X, 각 수열은 공백으로 구분해서 출력
                수열은 사전 순으로 증가하는 순서로 출력
"""
from sys import stdin


def solution(depth, n, m):
    if depth == m:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(len(visited)):
        if not visited[i]:  # 탐사를 하지 않았다면
            visited[i] = True
            out.append(i+1) # 탐사 내용
            solution(depth+1, n, m) # DFS
            visited[i] = False  # DFS 완료
            out.pop()   # 탐사 내용 제거


n, m = map(int, stdin.readline().split())
visited = [False] * n   # 탐사 여부 체크
out = []    # 출력 내용

solution(0, n, m)

"""
itertools 사용하기

from sys import stdin
from itertools import permutations

n, m = map(int, stdin.readline().split())
P = permutations(range(1, n+1), m)  # iter(tuple)
for i in P:
    print(' '.join(map(str, i)))  # tuple -> str
"""
