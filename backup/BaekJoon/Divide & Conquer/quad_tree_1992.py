"""
    쿼드트리(https://www.acmicpc.net/problem/1992)
     - 흰 점을 나타내는 0, 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자들의 점들이
        한 곳에 많이 몰려있으면, 쿼드트리에서는 이를 압축하여 간단히 표현할 수 있음
     - 주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 0, 모두 1로만 되어 있으면 압축 결과는 1
     - 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래,
        이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현
     - 입력 : 영상의 크기를 나타내는 숫자 N
                언제나 2의 제곱수로 주어지며, 1 <= N <= 64의 범위
             이후 N의 문자열이 N개, 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타냄

    * 참고 : https://wookcode.tistory.com/60
"""
from sys import stdin


def quad_tree(x, y, n):
    global result
    color = matrix[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != matrix[i][j]:   # 범위 안에 하나라도 다른 경우 4분면으로 나눠서 다시 검색
                result.append('(')      # 4분면으로 나눌 때 괄호를 침
                quad_tree(x, y, n//2)            # 2사분면
                quad_tree(x, y+n//2, n//2)       # 1사분면
                quad_tree(x+n//2, y, n//2)       # 3사분면
                quad_tree(x+n//2, y+n//2, n//2)  # 4사분면
                result.append(')')
                return
    result.append(color)    # 재귀로 안들어가거나 for문이 전부 끝난 상태일 경우 범위 안에 모든 수가 같다고 판단


n = int(stdin.readline().strip())
matrix = [list(map(int, stdin.readline().strip())) for _ in range(n)]
result = []

quad_tree(0, 0, n)
print("".join(map(str, result)))
