"""
    금광
     - n x m 크기의 금광, 1 x 1로 나뉘어 있음
     - 입력 : 테스트 케이스 T(1 <= T <= 100)
             매 테스트 케이스 첫째 줄에 n, m(1 <= n, m <= 20)
             둘째 줄에 n X m개의 위치에 매장된 금의 개수(0 <= 매장된 금의 개수 <= 100)
     - 출력 : 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기
"""
from sys import stdin

# 테스트케이스 입력
for tc in range(int(stdin.readline().strip())):
    # 금광 정보 입력
    n, m = map(int, stdin.readline().split())
    array = list(map(int, stdin.readline().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)