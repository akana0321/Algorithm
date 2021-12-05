"""
    가장 긴 증가하는 부분 수열 4(https://www.acmicpc.net/problem/14002)
     - 입력 : 수열 A의 크기 N(1 <= N <= 1,000)
             수열 A을 이루고 있는 Ai(1 <= Ai <= 1,000,000)
     - 출력 : 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
             그리고 가장 긴 증가하는 부분 수열 출력, 여러가지인 경우 아무거나 출력
"""
from sys import stdin

n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().split()))
dp = [1] * n

# 가장 긴 부분수열
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

count = max(dp)
print(count)

idx = dp.index(count)
result = []

# 긴 수열 찾아내기
while idx >= 0:
    if dp[idx] == count:
        result.append(nums[idx])
        count -= 1
    idx -= 1

result.reverse()
print(*result)
