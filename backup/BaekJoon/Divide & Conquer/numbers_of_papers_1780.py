"""
    종이의 개수(https://www.acmicpc.net/problem/1780)
     - NxN 크기의 행렬도 표현되는 종이가 있고, 각 칸에는 -1, 0, 1 중 하나가 저장
     - 규칙
        1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용
        2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서
            (1)의 과정을 반복한다
     - 이와 같이 종이를 잘랐을 때, -1, 0, 1로 채워진 각각의 종이의 개수를 구해내는 프로그램 작성
     - 입력 : 첫줄에 N(1 <= <= 3^7, N은 3^k꼴)
             이후 N개의 정수로 행렬이 주어진다
     - 출력 : 첫 줄에는 -1, 두번째 줄에는 0, 세번째 줄에는 1로 채워진 종이의 수를 출력

     * 참고 : https://velog.io/@uoayop/BOJ-1780-%EC%A2%85%EC%9D%B4%EC%9D%98-%EA%B0%9C%EC%88%98Python
"""
from sys import stdin

result = [0, 0, 0]


def solution(x, y, n):
    global result
    color = matrix[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != matrix[i][j]:
                solution(x, y, n//3)
                solution(x, y+n//3, n//3)
                solution(x, y+(2*n//3), n//3)
                solution(x+n//3, y, n//3)
                solution(x+n//3, y+n//3, n//3)
                solution(x+n//3, y+(2*n//3), n//3)
                solution(x+(2*n//3), y, n//3)
                solution(x+(2*n//3), y+n//3, n//3)
                solution(x+(2*n//3), y+(2*n//3), n//3)
                return

    if color == -1:
        result[0] += 1
    elif color == 0:
        result[1] += 1
    elif color == 1:
        result[2] += 1
    return


n = int(stdin.readline().strip())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
solution(0, 0, n)

for i in range(3):
    print(result[i])
