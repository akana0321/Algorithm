"""
    병든 나이트(https://www.acmicpc.net/problem/1783)

    * 참고 : https://pacific-ocean.tistory.com/354
"""
from sys import stdin

n, m = map(int, stdin.readline().split())

if n == 1 or m == 1:
    print(1)
elif n == 2:
    print(min(4, (m-1)//2+1))
elif m < 7:
    print(min(4, m))
else:
    print(m-2)
