"""
    색종이 만들기(https://www.acmicpc.net/problem/2630)

    * 참고 : https://claude-u.tistory.com/268
"""
from sys import stdin

# 쿼드 트리 함수 정의
def quad_tree(x, y, n):
    global matrix, blue, white # 주어진 배열과 색 카운트 끌어오기
    color = matrix[y][x]    # 첫 색깔과 나머지 색이 같아야 함
    double_break = False    # for문 탈출용

    for i in range(x, x+n):
        if double_break:
            break

        for j in range(y, y+n):
            if matrix[j][i] != color:       # 하나라도 다를 시 재귀문
                quad_tree(x, y, n//2)       # 2사분면
                quad_tree(x+n//2, y, n//2)  # 1사분면
                quad_tree(x, y+n//2, n//2)  # 3사분면
                quad_tree(x+n//2, y+n//2, n//2) # 4사분면
                double_break = True # 탈출
                break
    if not double_break:
        if matrix[y][x] == 1:   # 파란색
            blue += 1
        else:                   # 흰색
            white += 1


n = int(stdin.readline().strip())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
blue = 0
white = 0

quad_tree(0, 0, n)
print(white)
print(blue)
