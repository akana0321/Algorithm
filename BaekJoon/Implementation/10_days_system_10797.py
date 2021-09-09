"""
    10부제(https://www.acmicpc.net/problem/10797)
     - 입력 : 날짜의 일의자리 숫자
             5대의 자동차 번호의 일의자리 숫자
               날짜와 자동차의 일의 자리 숫자는 모두 0에서 9까지의 정수 중 하나이다
     - 출력 : 주어진 날짜와 자동차의 일의 자리 숫자를 보고 10부제를 위반하나는 차량의 대수 출력
"""
from sys import stdin

n = int(stdin.readline().strip())
cars = list(map(int, stdin.readline().split()))

print(cars.count(n))