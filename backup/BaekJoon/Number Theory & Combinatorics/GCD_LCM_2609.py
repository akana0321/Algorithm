"""
    최대공약수와 최소공배수(https://www.acmicpc.net/problem/2609)
     - 입력 : 두 개의 자연수(<= 10,000)
     - 출력 : 최대공약수
             최소공배수

     * 참고 : 유클리드 호제법 - https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
"""
from sys import stdin


def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n


def lcm(n, m):
    return n * m // gcd(n, m)


n, m = map(int, stdin.readline().split())

print(gcd(n, m))
print(lcm(n, m))
