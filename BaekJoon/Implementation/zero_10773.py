"""
    제로(https://www.acmicpc.net/problem/10773)
     - 입력 : 정수 K(1 <= K <= 100,000)
             이후 K개의 정수(0 <= 정수 <= 1,000,000)
             정수가 0인 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 씀
             정수가 0일 경우에 지울 수 있는 수가 있음을 보장할 수 있다
     - 출력 : 최종적으로 적어 낸 수의 합(<= 2^31 - 1)
"""
from sys import stdin

k = int(stdin.readline().strip())
nums = []

for _ in range(k):
    num = int(stdin.readline().strip())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))