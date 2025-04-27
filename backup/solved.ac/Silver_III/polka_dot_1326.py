"""
    폴짝폴짝(https://www.acmicpc.net/problem/1326)
"""

from sys import stdin
from collections import deque

def bfs(start, end, bridge, n):
    q = deque()
    q.append(start - 1)
    check = [-1] * n
    check[start - 1] = 0
    while q:
        node = q.popleft()
        for i in range(node, n, bridge[node]):
            if check[i] == -1:
                q.append(i)
                check[i] = check[node] + 1
                if i == end - 1:
                    return check[i]
        for i in range(node, -1, -bridge[node]):
            if check[i] == -1:
                q.append(i)
                check[i] = check[node] + 1
                if i == end - 1:
                    return check[n]
    return -1

n = int(stdin.readline().strip()) # 전체 징검다리 수
bridge = list(map(int, stdin.readline().split())) # 징검다리에 적혀있는 수
start, end = map(int, stdin.readline().split()) # 출발, 도착지

print(bfs(start, end, bridge, n))
