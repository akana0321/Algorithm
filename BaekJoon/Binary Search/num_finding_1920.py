"""
    수 찾기(https://www.acmicpc.net/problem/1920)
     - 입력 : 자연수 N(1 <= N <= 100,000)
             이후 N개의 정수 A[1], A[2], ...., A[n]
             다음 M(1 <= M <= 100,000)
             이후 M개의 수가 주어지는데, 이 수들이 A 안에 존재하는지 알아내면 됨
             모든 정수의 범위는 -2^31보다 크거나 같고 2^31보다 작다

    * 참고거리 : https://wook-2124.tistory.com/451
"""
from sys import stdin


def binary_search(start, end, target):
    mid = (start + end) // 2

    if nums[mid] == target:
        print(1)
    elif nums[mid] > target and mid != start:
        binary_search(start, mid-1, target)
    elif nums[mid] < target and mid != end:
        binary_search(mid+1, end, target)
    else:
        print(0)


n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().split()))
nums.sort()
m = int(stdin.readline().strip())
targets = list(map(int, stdin.readline().split()))

for target in targets:
    binary_search(0, len(nums)-1, target)

"""
# 위 링크에 있는 방법 : set으로 변환하여 접근, set에서의 탐색은 O(1)이라고 한다
numSet = set(nums)

for target in targets:
    if target in numSet:
        print(1)
    else:
        print(0)
"""