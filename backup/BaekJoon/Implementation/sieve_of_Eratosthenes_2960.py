"""
    에라토스테네스의 체(https://www.acmicpc.net/problem/2960)
    
"""
from sys import stdin

n, k = map(int, stdin.readline().split())
nums = [True] * (n + 1)
count = 0

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if nums[j]:
            nums[j] = False
            count += 1
            if count == k:
                print(j)
                break
