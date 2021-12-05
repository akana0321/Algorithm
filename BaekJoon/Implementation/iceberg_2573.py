"""
    빙산(https://www.acmicpc.net/problem/2573)

    * 참고 : https://bbbyung2.tistory.com/67
"""
from sys import stdin
from collections import deque
from copy import deepcopy
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def count_ocean(x, y, temp_iceberg):
    count = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and temp_iceberg[nx][ny] == 0:
            count += 1
    return count


def count_iceberg(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


def solution():
    global visited, result
    while True:
        visited = [[False] * m for _ in range(n)]
        piece = 0
        # 빙산이 다 녹을 때까지 분리되지 않는 경우
        flag = True
        for i in range(n):
            for j in range(m):
                if iceberg[i][j] != 0:
                    flag = False
        if flag:
            print(0)
            return

        # 빙산이 녹은 이후로 업데이트
        temp_iceberg = deepcopy(iceberg)
        for i in range(1, n-1):
            for j in range(1, m-1):
                if temp_iceberg[i][j] != 0:
                    iceberg[i][j] = max(0, iceberg[i][j] - count_ocean(i, j, temp_iceberg))

        # 빙산의 개수 세기
        for i in range(1, n-1):
            for j in range(1, m-1):
                if not visited[i][j] and iceberg[i][j] != 0:
                    count_iceberg(i, j)
                    piece += 1

        if piece >= 2:
            print(result)
            return

        result += 1


n, m = map(int, stdin.readline().split())
iceberg = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = []
result = 1
solution()
