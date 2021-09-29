"""
    N-Queen(https://www.acmicpc.net/problem/9663)
     - 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓은 문제
        N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램 작성
     - 입력 : N(1 <= N < 15)
     - 출력 : 퀸 N개를 서로 공격할 수 없게 놓은 경우의 수를 출력

     참고 : https://hellominchan.tistory.com/176
"""
from sys import stdin


def dfs(i):
    global n, col, slash, backSlash, case

    if i == n:
        case += 1
        return
    for j in range(n):
        if not(col[j] or slash[i+j] or backSlash[i-j+n-1]):
            col[j] = slash[i+j] = backSlash[i-j+n-1] = True
            dfs(i+1)
            col[j] = slash[i+j] = backSlash[i-j+n-1] = False


n = int(stdin.readline().strip())
col, slash, backSlash = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
case = 0

dfs(0)

print(case)
