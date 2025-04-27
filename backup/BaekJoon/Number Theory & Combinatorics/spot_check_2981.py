"""
    검문(https://www.acmicpc.net/problem/2981)
     - N개의 숫자를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다
     - 입력 : 종이에 적은 수의 개수 N(2 <= N <= 100)
             이후 N개의 줄에는 수가 주어임(1 <= 적은 수 <= 1,000,000,000)
                같은 수가 두 번 이상 주어지지 않으며 M이 하나 이상 존재하는 경우만 입력으로 주어짐
     - 출력 : 가능한 모든 M을 공백으로 구분하여 모두 출력(오름차순)

     * 참고 : https://claude-u.tistory.com/260
"""
from sys import stdin


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 약수 리스트를 구하는 함수
def div(x):
    div_list = [x]
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            div_list.append(i)
            if x // i != i:
                div_list.append(x//i)
    div_list.sort()
    return div_list


n = int(stdin.readline().strip())
nums = [int(stdin.readline().strip()) for _ in range(n)]
nums.sort()

# 숫자들의 차이 입력
nums_diff = []
for i in range(len(nums)-1):
    nums_diff.append(nums[i+1] - nums[i])

# 숫자들의 차이를 최대공약수를 이용하여 구하기
if len(nums_diff) == 1:
    answer = nums_diff[0]
elif len(nums_diff) == 2:
    answer = gcd(nums_diff[0], nums_diff[1])
else:
    answer = nums_diff[0]
    for i in range(1, len(nums_diff)):
        answer = gcd(answer, nums_diff[i])

for i in div(answer):
    print(i, end=' ')
