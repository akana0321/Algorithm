"""
    2048(easy) (https://www.acmicpc.net/problem/12100)
     - 입력 : 보드의 크기 N(1 <= N <= 20)
             게임판의 초기의 상태
                0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다
                블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴
                적어도 블록은 하나 이상 주어짐
     - 출력 : 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 출력

    * 참고 : https://jeongchul.tistory.com/667
"""
from sys import stdin
from collections import deque


def get(i, j):
    if board[i][j] != 0:
        q.append(board[i][j])
        board[i][j] = 0


def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        if board[i][j] == 0:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x*2
            i, j = i+di, j+dj
        else:
            i, j = i+di, j+dj
            board[i][j] = x


def move(k):
    if k == 0:      # 위로 이동
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:    # 아래로 이동
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0)
    elif k == 2:    # 오른쪽으로 이동
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else:           # 왼쪽으로 이동
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1)


def solve(count):
    global board, answer
    if count == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]

    for k in range(4):
        move(k)
        solve(count+1)
        board = [x[:] for x in b]


n = int(stdin.readline().strip())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer, q = 0, deque()
solve(0)
print(answer)
