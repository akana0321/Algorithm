"""
    방 번호(https://www.acmicpc.net/problem/1475)
     - 입력 : 방 번호 N(<= 1,000,000)
     - 출력 : 필요한 세트의 개수
"""
from sys import stdin

num_set = [0] * 10
room_nums = list(map(int, stdin.readline().strip()))

for room_num in room_nums:
    num_set[room_num] += 1

if (num_set[6] + num_set[9]) % 2 == 1:
    num_set[6] = (num_set[6] + num_set[9]) // 2 + 1
    num_set[9] = 0
else:
    num_set[6] = (num_set[6] + num_set[9]) // 2
    num_set[9] = 0

print(max(num_set))