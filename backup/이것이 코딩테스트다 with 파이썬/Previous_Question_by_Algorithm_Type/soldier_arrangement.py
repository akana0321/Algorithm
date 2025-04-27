"""
    병사 배치(https://www.acmicpc.net/problem/18353)
     - 병사 배치 시 전투력이 높은 병사가 앞에 오도록 내림차순으로 배치
     - 배치 시에 특정 위치의 병사들을 열외, 그러면서도 남아있는 병사의 수가 최대가 되도록
     - 입력 : 병사의 수N(1 <= N <= 2,000)
             이후 병사의 전투력이 공백으로 구분되어 주어짐(<= 10,000,000)
     - 출력 : 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수
"""
from sys import stdin
input = stdin.readline

''' 처음 풀었던 거
n = int(input().strip())
combat_power = list(map(int, input().split()))
save_index = []

for i in range(n - 1):
    if combat_power[i] < combat_power[i + 1]:
        save_index.append(i + 1)

print(len(save_index))
'''
n = int(input().strip())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))