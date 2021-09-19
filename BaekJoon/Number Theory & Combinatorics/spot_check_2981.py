"""
    검문(https://www.acmicpc.net/problem/2981)
     - N개의 숫자를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다
     - 입력 : 종이에 적은 수의 개수 N(2 <= N <= 100)
             이후 N개의 줄에는 수가 주어임(1 <= 적은 수 <= 1,000,000,000)
                같은 수가 두 번 이상 주어지지 않으며 M이 하나 이상 존재하는 경우만 입력으로 주어짐
     - 출력 : 가능한 모든 M을 공백으로 구분하여 모두 출력(오름차순)
"""
from sys import stdin


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(stdin.readline().strip())
nums = [int(stdin.readline().strip()) for _ in range(n)]
minimum = min(nums)

for i in range(len(nums)):
    if nums[i] > minimum:
        nums[i] -= minimum
nums.remove(minimum)

gcd_num = nums[0]
for i in range(len(nums)):
    gcd_num = gcd(gcd_num, nums[i])

print(gcd_num)

for i in range(2, gcd_num + 1):
    if gcd_num % i == 0:
        print(i, end=' ')