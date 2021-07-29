"""
    편집 거리
     - 두 개의 문자열 A와 B가 주어졌을 때, A -> B로 하려 함
      1. 삽입(Insert) : 특정한 위치에 하나의 문자를 삽입
      2. 삭제(Remove) : 특정 위치에 있는 하나의 문자를 삭제
      3. 교체(Replace) : 특정한 위치에 있는 하나의 문자를 다른 문자로 교체
     - 여기서 편집 거리란 A -> B로 바꾸는 연산의 수
     - 입력 : A와 B가 한 줄에 하나씩 주어짐(1 <= 각 문자열의 길이 <= 5,000)
     - 출력 : 최소 편집 거리
"""
''' 처음 했던거
from sys import stdin

a = list(stdin.readline().strip())
b = list(stdin.readline().strip())
count = 0

for i in range(len(b)):
    if a[i] != b[i]:
        count += 1
        if len(a) < len(b): # 삽입
            a.insert(i, b[i])
        elif len(a) > len(b):
            a.pop(i)
        else:
            a[i] = b[i]

print(count)
'''
from sys import stdin

# 최소 편집 거리(Edit Distance) 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 다이믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면 3가지 경우 중에서 최소 비용을 찾아 대입
            else: # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]

# 두 문자열을 입력받기
str1 = stdin.readline().strip()
str2 = stdin.readline().strip()

print(edit_dist(str1, str2))