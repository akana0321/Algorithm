"""
    랜선 자르기(https://www.acmicpc.net/problem/1654)
     - 입력 : 이미 갖고 있는 랜선의 개수 K, 필요한 랜선의 개수 N(1 <= K <= 10,000, 1 <= N <= 1,000,000, 항상 K <= N)
              이후 이미 갖고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력(<=2^31 - 1)
     - 출력 : N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력
"""
# 이진탐색으로 풀어야 한다
from sys import stdin

K, N = map(int, stdin.readline().split())
lan = [int(stdin.readline()) for _ in range(K)]
start, end = 1, max(lan) # 이진탐색의 처음과 끝

while start <= end: # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 # 중간점
    lines = 0
    for i in lan:
        lines += i // mid # 분할된 랜선의 수

    if lines >= N: # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1

print(end)