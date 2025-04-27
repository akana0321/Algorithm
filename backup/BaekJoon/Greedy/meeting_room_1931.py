"""
    회의실 배정(https://www.acmicpc.net/problem/1931)
     - 입력 : 회의의 수 N(1 <= N <= 100,000)
             이후 회의의 정보가 주어지는데 회의 시작 시간과 끝나는 시간(<= 2^31 - 1)
     - 출력 : 최대 사용할 수 있는 회의의 최대 갯수
"""
from sys import stdin

n = int(stdin.readline().strip())
info = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
info.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = info[0][1]

for i in range(1, n):
    if info[i][0] >= end_time:
        count += 1
        end_time = info[i][1]

print(count)