"""
    카드 정렬하기(https://www.acmicpc.net/problem/1715)
     - 카드 묶음 A와 B를 합칠 때 A + B번을 비교해야 함
     - 예를 들어 10, 20, 40장의 카드를 합칠 때 (10 + 20) + (30 + 40) = 100번의 비교가 필요
       (10 + 40) + (50 + 20) = 120의 방법도 있으나 비효율적
     - 입력 : 카드 묶음의 갯수 N(1 <= N <= 100,000)
             N줄에 걸쳐 각각의 카드 수
     - 출력 : 최소 비교 횟수
"""
from sys import stdin
import heapq

n = int(stdin.readline().strip())
result = 0
# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(stdin.readline().strip())
    heapq.heappush(heap, data)

# 힙에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    card1 = heapq.heappop(heap)
    card2 = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = card1 + card2
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)