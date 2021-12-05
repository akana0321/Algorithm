"""
    나이트의 이동(https://www.acmicpc.net/problem/7562)
     - 입력 : 테스트 케이스의 개수
             테스트 케이스는 세 줄로 이루어져 있는데 첫 째줄에는 체스판 한 변의 길이 l(4 <= l <= 300), 체스판의 크기는 l x l
                체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} x {0, ..., l-1}로 나타낼 수 있다
             둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다
     - 출력 : 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력
"""
from sys import stdin
from collections import deque
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


def bfs(start, target, board):
    dq = deque()
    dq.append([start[0], start[1]])
    board[start[0]][start[1]] = 1

    while dq:
        x, y = dq.popleft()
        if x == target[0] and y == target[1]:
            return board[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] == 0:
                    dq.append([nx, ny])
                    board[nx][ny] = board[x][y] + 1


def check_print(start, target, board):
    if start == target:
        print(0)
    else:
        print(bfs(start, target, board))


for _ in range(int(stdin.readline().strip())):
    length = int(stdin.readline().strip())
    board = [[0] * length for _ in range(length)]
    start = list(map(int, stdin.readline().split()))
    target = list(map(int, stdin.readline().split()))
    check_print(start, target, board)
