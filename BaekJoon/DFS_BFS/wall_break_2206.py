"""
    벽 부수고 이동하기(https://www.acmicpc.net/problem/2206)
     - NxM의 행렬로 표현되는 맵, 0은 이동할 수 있고 1은 이동할 수 없는 벽
        (1, 1)에서 (N, M)의 위치까지 이동하려는데 최단 경로로 이동하려 함(시작, 목적지 칸 포함)
     - 만약 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 짧아지면 벽을 한 개까지 부숴도 됨
        한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸
     - 입력 : N M(1 <= N, M <= 1,000)
             이후 맵의 정보, (1, 1)과 (N, M)은 항상 0이라 가정
     - 출력 : 최단 거리 출력, 불가능할 때는 -1 출력
"""
from sys import stdin
from collections import deque


def bfs(n, m, graph):
    dx = [1, 0, -1, 0]
    dy = dx[::-1]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    dq = deque([])
    dq.append([0, 0, 1])

    while dq:
        x, y, isDestroyed = dq.popleft()
        if x == n - 1 and y == m -1:
            return visited[x][y][isDestroyed]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and isDestroyed == 1:
                    visited[nx][ny][0] = visited[x][y][isDestroyed] + 1
                    dq.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visited[nx][ny][isDestroyed] == 0:
                    visited[nx][ny][isDestroyed] = visited[x][y][isDestroyed] + 1
                    dq.append([nx, ny, isDestroyed])
    return -1


n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]
print(bfs(n, m, graph))
