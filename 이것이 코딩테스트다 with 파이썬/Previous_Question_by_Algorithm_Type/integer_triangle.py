"""
    정수 삼각형
     - 맨 위부터 시작해서 내려오는데 대각선으로만 이동 가능
     - 입력 : 삼각형의 크기 n(1 <= n <= 500), 이후 정수 삼각형이 주어짐
     - 출력 : 합이 최대가 되는 경로에 있는 수의 합
"""
from sys import stdin

n = int(stdin.readline().strip())
dp = [list(map(int, stdin.readline().split())) for _ in range(n)]

# 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))