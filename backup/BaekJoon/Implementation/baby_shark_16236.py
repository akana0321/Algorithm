"""
    아기 상어(https://www.acmicpc.net/problem/16236)
     * 참고 : https://dailyheumsi.tistory.com/59
"""
from sys import stdin
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def shark_point():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                return i, j


def bfs(x, y):
    q, visited = deque([(x, y)]), set([(x, y)])
    time = 0
    shark = 2
    eat = 0
    eat_flag = False
    answer = 0

    while q:
        size = len(q)
        # 위와 왼쪽을 우선으로 가야하기 때문에 q를 정렬해줌
        q = deque(sorted(q))
        for _ in range(size):
            x, y = q.popleft()
            # 작은 물고기가 있어서 먹은 경우
            if board[x][y] != 0 and board[x][y] < shark:
                board[x][y] = 0
                eat += 1
                # 크기만큼 먹었으면 크기 늘리고 먹은 수 초기화
                if eat == shark:
                    shark += 1
                    eat = 0

                # 먹고 난 후 현재 위치 기준으로 BFS 해야하기 때문에 큐와 visited 초기화
                q, visited = deque(), set([x, y])
                eat_flag = True
                # 먹었을 때 시간 저장
                answer = time

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if board[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            # 현재 위치에서 먹었다면 for문 탈출
            if eat_flag:
                eat_flag = False
                break
        time += 1
    return answer


n = int(stdin.readline().strip())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
s_x, s_y = shark_point()
print(bfs(s_x, s_y))
