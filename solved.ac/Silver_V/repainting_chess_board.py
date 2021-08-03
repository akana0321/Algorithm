"""
    체스판 다시 칠하기
     - 입력 : N M(1 <= N, M <= 50)
             보드의 각 행의 상태가 주어지는데, B는 검정, W는 하양
     - 출력 : 다시 칠해야 하는 정사각형 개수의 최솟값

     * 최대 50 * 50 크기 -> 8 * 8 크기로 자르는 모든 경우를 고려한다 해도 43 * 43 가지
        => 연산하기에 충분히 작은 수 이므로 모든 경우 고려 가능
     * 체스판 시작이 흰색일 때와 검정색일 때가 색칠하는 패턴이 다르므로 고려해야 함
     * 8 * 8로 자른 것을 순회하면서 색칠해야 하는 부분을 1, 안해도 되는 부분을 0으로 구성한 배열을 새로 만듬
       -> 최종적으로 이를 합해서 작은 것을 저장

    20210803 - 문제
8 8
WWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
이거 넣었을 때 첫번째만 바꿔서 1이 나와야 하는데 63이 나옴..
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
board = [[0] * m for _ in range(n)]
white_first = []
black_first = []

for i in range(n):
    row = stdin.readline().strip()
    for j in range(m):
        board[i][j] = row[j]

initial = board[0][0]

# 흰색으로 시작하는 체스판을 만드는 경우
for i in range(n):
    painting = []
    if i % 2 == 0:
        current_color = 'W'
    else:
        current_color = 'B'

    for j in range(m):
        if board[i][j] == current_color:
            painting.append(0)
        else:
            painting.append(1)

        if current_color == 'W':
            current_color = 'B'
        else:
            current_color = 'W'
    white_first.append(painting)

# 검은색으로 시작하는 체스판을 만들 경우
for i in range(n):
    painting = []
    if i % 2 == 0:
        current_color = 'B'
    else:
        current_color = 'W'

    for j in range(m):
        if board[i][j] == 'W':
            painting.append(0)
        else:
            painting.append(1)

        if current_color == 'W':
            current_color = 'B'
        else:
            current_color = 'W'

    black_first.append(painting)

# 최솟값을 초기화할 때 보드의 최대 크기인 50*50으로 설정
min_count = 50 * 50
for i in range(n - 8 + 1):
    rows = white_first[i:i + 8]
    for j in range(m - 8 + 1):
        paint = 0
        for row in rows:
            paint += sum(row[j:j + 8])
        if paint < min_count:
            min_count = paint

print(min_count)
