"""
    분해합(https://www.acmicpc.net/problem/2231)
     - 어떤 자연수 N의 분해합은 N을 이루는 각 자리수의 합을 의미
     - 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성
"""
from sys import stdin

n = int(stdin.readline().strip())
result = 0

for i in range(1, n + 1):
    elements = list(map(int, str(i)))
    result = i + sum(elements)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
