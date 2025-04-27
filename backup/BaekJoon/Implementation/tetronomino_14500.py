"""
    테트로노미노(https://www.acmicpc.net/problem/14500)
     - 입력 : 종이의 세로의 크기 N과 가로 크기 M(4 <= N, M <= 500)
             이후 종이에 쓰여 있는 수, 1,000을 넘지 않음
     - 출력 : 테트로노미노가 놓인 칸에 쓰인 수들의 합의 최댓값 출력

      * https://jeongchul.tistory.com/670 참고고
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer = 0
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

def find(x, y):
    global answer
    for i in range(19): # 테트로미노가 19가지 모양
        result = 0      # 각 테트로미노의 합산 값을 더함
        for j in range(4):  # 테트로미노는 4개의 블록으로 구성
            try:
                next_x = x + tetromino[i][j][0] # 현재 위치에서 테트로미노를 놓은 x좌표
                next_y = y + tetromino[i][j][1] # 현재 위치에서 테트로미노를 놓은 y좌표
                result += board[next_x][next_y] # 합산 값
            except IndexError:  # 현재 위치에서 테트로미노가 board 밖으로 나가게 된다면 인덱스 에러 발생
                continue        # 패스
        answer = max(answer, result)    # 최대값을 저장

def solve():
    for i in range(n):
        for j in range(m):
            find(i, j)

solve()
print(answer)

