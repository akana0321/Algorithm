"""
    사분면 고르기(https://www.acmicpc.net/problem/14681)
     - 입력 : x / y (-1000 <= x, y <= 1000, x,y는 0이 아님)
     - 출력 : 속해있는 사분면의 번호
"""
from sys import stdin

x = int(stdin.readline())
y = int(stdin.readline())

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and  y > 0:
    print(2)
else:
    print(3)