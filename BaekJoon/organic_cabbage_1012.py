"""
    유기농 배추(https://www.acmicpc.net/problem/1012)
     - 입력 : 테스트 케이스의 개수
             배추밭의 가로길이 M N(1 <= M, N <= 50) 배추가 심어져 있는 위치의 개수 K(1 <= K <= 2500)
             이후 배추의 위치 X(0 <= X <= M-1) Y(0 <= Y <= N-1)
     - 출력 : 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수
"""
from sys import stdin
from collections import deque

dx = [-1, 0, 1, 0]
dy = dx[::-1]


def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


for _ in range(int(stdin.readline().strip())):
    count = 0
    n, m, k = map(int, stdin.readline().split())
    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, stdin.readline().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                count += 1

    print(count)
