"""
    미로찾기(https://www.acmicpc.net/problem/2178)
     -
"""
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = dx[::-1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))

