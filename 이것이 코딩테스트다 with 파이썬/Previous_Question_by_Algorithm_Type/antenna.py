"""
    안테나
     - 집에다가 안테나 설치, 각각의 집까지의 거리가 가장 가까운 곳에 설치
     - 입력 : 집의 수 N(1 <= N <= 200,000)
     - 출력 : 가장 가까운 위치의 집, 여러 개의 값이 도출될 경우 가장 작은 수 출력
"""
from sys import stdin
n = int(stdin.readline().strip())
house = list(map(int, stdin.readline().split()))
house.sort()

print(house[(n - 1) // 2])