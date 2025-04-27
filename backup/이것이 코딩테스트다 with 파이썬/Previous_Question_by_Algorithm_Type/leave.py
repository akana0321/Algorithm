"""
    퇴사
     - 입력 : 일을 할 수 있는 날 N(1 <= N <= 15)
             이후 Ti와 Pi가 주어지며 1일부터 N일까지 순서대로 주어짐(1 <= Ti <= 5, 1 <= Pi <= 1,000)
     - 출력 : 최대 이익
"""
from sys import stdin
input = stdin.readline

n = int(input().strip())
t = [] # 상담 시간
p = [] # 상담 금액
dp = [0] * (n + 1) # dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
