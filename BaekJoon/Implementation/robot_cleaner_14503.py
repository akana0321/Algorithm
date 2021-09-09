"""
    로봇 청소기(https://www.acmicpc.net/problem/14503)
     - 입력 : 첫째 줄에 세로의 크기 N, 가로의 크기 M(3 <= N, M <= 50)
             둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바로보는 방향 d
               d가 0인 경우에는 북, 1이면 동, 2이면 남, 3이면 서쪽
             셋째 줄부터는 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어짐
               빈칸은 0, 벽은 1, 지도의 첫, 마지막 행과 열은 모든 칸이 벽
     - 출력 : 로봇 청소기가 청소하는 칸의 개수
"""
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
start = list(map(int, stdin.readline().split()))
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

check = [[0 for _ in range(m)] for _ in range(n)]
check[start[0]][start[1]] = 1
count = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque([start])

while q:
    r, c, d = q.popleft()
    nd = d
    move = 0

    for i in range(4):
        nd -= 1
        if nd < 0:
            nd = 3

        nr = r + dx[nd]
        nc = c + dy[nd]

        if 0 <= nr < n and 0 <= nc < m:
            if board[nr][nc] == 0 and check[nr][nc] == 0:
                check[nr][nc] = 1
                q.append([nr, nc, nd])
                count += 1
                move = 1
                break

    if move == 1:
        continue
    else:
        nr = r - dx[nd]
        nc = c - dy[nd]
        if 0 <= nr <n and 0 <= nc < m:
            if board[nr][nc] == 0:
                q.append([nr, nc, nd])

print(count)
