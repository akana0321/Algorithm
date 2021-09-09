"""
    뱀(https://www.acmicpc.net/problem/3190)
     - N x N 정사각 보드위에 몇몇 칸에는 사과가 있음
     - 보드 상하좌우 끝에 벽이 있다
     - 시작 시 뱀은 맨 위 좌측에 위치하고 뱀의 길이는 1, 처음에 오른쪽을 향함
     - 벽 또는 자기자신의 몸과 부딪히면 게임 끝
     - 이동 규칙
       * 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킴
       * 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
       * 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌. 즉, 몸길이는 변하지 않는다
     - 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇오에 끝나는지 계산
     - 입력 : 보드의 크기 N(2 <= N <= 100)
             사과의 개수 K(0 <= K <= 100)
             이후 가과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미
               사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열)에는 사과가 없다
             뱀의 방향 변환 횟수 L(1 <= L <= 100)
             이후 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며, 게임 시작 시간으로부터
               X초가 끝난 뒤에 왼쪽(C가 'L')또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다
               X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어미
     - 출력 : 게임이 몇 초에 끝나는지 출력
"""
from sys import stdin

n = int(stdin.readline().strip())
k = int(stdin.readline().strip())
board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, stdin.readline().split())
    board[x][y] = 1

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
    x, y = 1, 1     # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0   # 처음에는 동쪽을 보고 있음
    time = 0        # 시작한 뒤에 지난 '초' 시간
    index = 0       # 다음에 회전할 정보
    q = [(x, y)]    # 뱀이 차지하고 있는 위치 정보(고리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        print(nx, ny)
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())