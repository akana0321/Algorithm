"""
    다리 놓기(https://www.acmicpc.net/problem/1010)
     - 입력 : 테스트 케이스의 개수 T
             이후 서쪽과 동쪽에 있는 사이트의 개수 N, M(0 < N <+ M < 30)
     - 출력 : 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수
"""
from sys import stdin

def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

for tc in range(int(stdin.readline().strip())):
    n, m = map(int, stdin.readline().split())
    bridge = factorial(m) // (factorial(m - n) * factorial(n))
    print(bridge)