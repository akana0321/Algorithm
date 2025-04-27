"""
    경쟁적 전염(https://www.acmicpc.net/problem/18405)
     - 입력 : n, k(1 <= n <= 200, 1 <= k <= 100)
             이후 N개의 줄에 걸쳐 시험관의 정보, 바이러스가 존재하지 않는 곳은 0으로 주어짐
             N + 2번 줄에는 S, X, Y가 주어지며, 공백으로 구분(0 <= S <= 10,000, 1 <= X, Y <= N)
     - 출력 : S초 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력
             만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면 0을 출력
"""
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트
for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스의 종류, 시간, x좌표, y좌표) 삽입
            data.append((graph[i][j], 0, i, j))
# 낮은 번호의 바이러스가 우선 증식하므로 정렬 이후에 큐로 옮기기
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, stdin.readline().split())

dx = [-1, 0, 1, 0]
dy = dx[::-1]

# BFS
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx <n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])