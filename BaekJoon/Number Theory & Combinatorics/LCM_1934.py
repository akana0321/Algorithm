"""
    최소공배수(https://www.acmicpc.net/problem/1934)
     - 입력 : 테스트 케이스의 개수 T(1 <= T <= 1,000)
             이후 A와 B(1 <= A, B <= 45,000)
     - 출력 : T개의 줄에 A와 B의 최소 공배수를 한 줄에 하나씩 출력
"""
from sys import stdin


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


for _ in range(int(stdin.readline().strip())):
    a, b = map(int, stdin.readline().split())
    print(lcm(a, b))
