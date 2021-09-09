"""
    뱀 (dx, dy 기초 - 못품20210720)
     - 뱀은 처음에 오른 쪽으로 향함
     - 규칙
        1. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킴
        2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
        3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌. 즉, 몸 길이는 변하지 않음
     - 입력 : 보드의 크기 N(2 <= N <= 100), 사과의 개수 K(0 <= K <= 100)
             이후 K개의 줄에는 사과의 위치, 행 열 으로 입력이 주어지고 (1, 1)에는 사과가 없음
             다음은 뱀의 방향 변환 횟수 L(1 <= L <= 100)
             다음 L개의 줄에는 X C가 주어지는데, 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 L) 또는 오른쪽(C가 R)으로
             90도 회전시킨다는 뜻(X <= 10,000)
     - 출력 : 게임이 끝나는 시각
"""
from sys import stdin

n = int(stdin.readline().strip()) # 보드의 크기
k = int(stdin.readline().strip()) # 사과의 갯수
board = [[0] * (n + 1) for _ in range(n + 1)] # 보드 초기화
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    board[a][b] = 1 # 사과가 있는 자리를 1로 교체

l = int(stdin.readline().strip()) # 방향 변환 횟수
info = [] # 방향 변환 정보
for _ in range(l):
    x, c = stdin.readline().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위ㅣ
    board[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 보드 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리는 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index <l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())