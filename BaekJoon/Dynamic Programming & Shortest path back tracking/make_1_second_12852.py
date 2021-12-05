"""
    1로 2 만들기 2(https://www.acmicpc.net/problem/12852)
     - 정수 x에 사용할 수 있는 연산은 다음과 같은 3가지
        1. x가 3으로 나우어 떨어지면, 3으로 나눈다
        2. x가 2로 나누어 떨어지면, 2로 나눈다
        3. 1을 뺀다
     - 정수 N이 주어졌을 때 위 세 개의 연산을 적절히 사용해서 1을 만드는 최소 횟수
     - 입력 : 1보다 크거나 같고 10^6보다 작거나 같은 자연수 N
     - 출력 : 연산을 하는 횟수의 최솟값 출력
             이후 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 출력
                정답이 여러 가지인 경우에는 아무거나 출력
"""
from sys import stdin


def solution():
    global n, dp
    for i in range(2, n + 1):
        # f(x-1) + 1
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = dp[i-1][1] + [i]

        # f(x//3) + 1
        if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i//3][0] + 1
            dp[i][1] = dp[i//3][1] + [i]

        # f(x//2) + 1
        if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i//2][0] + 1
            dp[i][1] = dp[i//2][1] + [i]


def printSolution():
    global n, dp
    print(dp[n][0])
    for i in dp[n][1][::-1]:
        print(i, end=' ')


n = int(stdin.readline().strip())

dp = [[0, []] for _ in range(n + 1)]    # [최솟값, [경로 리스트]]
dp[1][0] = 0    # 최솟값
dp[1][1] = [1]  # 경로를 담을 리스트

solution()
printSolution()
