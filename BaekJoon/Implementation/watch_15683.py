"""
    감시(https://www.acmicpc.net/problem/15683)
     - CCTV의 종류
       * 1번 : 한 방향만
       * 2번 : 두 방향(서로 대칭)
       * 3번 : 두 방향(수직)
       * 4번 : 세 방향(ㅗ)
       * 5번 : 네 방향(상하좌우)
     - 벽이 있으면 막히고, CCTV끼리는 관통 가능
     - 입력 : 사무실ㄹ의 세로 크기 N, 가로 크기 M(1 <= N, M <= 8)
             이후 사무실 정보, 0은 빈 칸, 6은 벽, 1 ~ 5는 CCTV
             CCTV의 최대 개수는 8개를 넘지 않는다
     - 출력 : 사각 지대의 최소 크기
"""
from sys import stdin
from collections import deque
from copy import deepcopy

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(count):
    global ans, temp_a
    if count == len(cctv):
        temp_a = deepcopy(a)
        c = 0
        for i in range(len(cctv)):
            x, y = cctv[i]
            if a[x][y] == 1:
                c += move(x, y, dir[i])
            elif a[x][y] == 2:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 2) % 4)
            elif a[x][y] == 3:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)
            else:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)
                c += move(x, y, (dir[i] + 2) % 4)
        ans = min(ans, area - c)
        return

    for i in range(4):
        dir.append(i)
        dfs(count + 1)
        dir.pop()


def move(x, y, d):
    count = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if not 0 <= nx < N or not 0 <= ny < M or temp_a[nx][ny] == 6:
            return count
        if 0 < temp_a[nx][ny] < 6 or temp_a[nx][ny] == -1:
            x, y = nx, ny
            continue
        temp_a[nx][ny] = -1
        count += 1
        x, y = nx, ny


N, M = map(int, stdin.readline().split())
area = N * M
a, cctv, cctv5 = [], [], []
for i in range(N):
    row = list(map(int, stdin.readline().split()))
    a.append(row)
    for j in range(M):
        if 0 < a[i][j] < 5:
            cctv.append([i, j])
            area -= 1
        elif a[i][j] == 5:
            cctv5.append([i, j])
            area -= 1
        elif a[i][j] == 6:
            area -= 1

    for i in range(len(cctv5)):
        x, y = cctv5[i]
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if not 0 <= nx < N or not 0 <= ny < M or a[nx][ny] == 6:
                    break
                if 0 < a[nx][ny] < 6 or a[nx][ny] == -1:
                    continue
                a[nx][ny] -= 1
                area -= 1

dir = deque()
ans = area
dfs(0)
print(ans)