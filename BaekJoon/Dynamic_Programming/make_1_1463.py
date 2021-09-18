"""
    1로 만들기(https://www.acmicpc.net/problem/1463)
     - X가 3으로 나누어 떨어지면, 3으로 나눈다
     - X가 2로 나누어 떨어지면, 2로 나눈다
     - 1을 뺀다
     - 위의 세 연산을 적절히 사용해서 1을 만들 때 연산의 최소횟수
     - 입력 : 정수 N(1 <= N <= 1000000)
     - 출력 : 연산의 최소 횟수
"""
from sys import stdin

n = int(stdin.readline().strip())