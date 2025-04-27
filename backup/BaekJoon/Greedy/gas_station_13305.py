"""
    주유소(https://www.acmicpc.net/problem/13305)
     - 입력 : 도시의 개수 N(2 <= N <= 100,000)
             두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터 N - 1개의 자연수로 주어짐
             주유소의 리터당 가격이 제일 왼쪽부터 N개의 자연수로 주어짐
                제일 왼쪽 도시부터 제일 오른쪽 도시까지의 거리는 1이상 1,000,000,000 이하의 자연수
                리터당 가격은 1 이상 1,000,000,000 이하의 자연수
     - 출력 : 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력
"""
from sys import stdin

n = int(stdin.readline().strip())
distance = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))

result = 0
minCost = cost[0]

for i in range(n - 1):
    if cost[i] < minCost:
        minCost = cost[i]
    result += minCost * distance[i]

print(result)