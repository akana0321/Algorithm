"""
    가운데를 말해요(https://www.acmicpc.net/problem/1655)
      - 정수가 하나 주어질 때마다 지금까지 주어진 수 중에서 중간값을 말해야 함
            만약 외친 수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 함
      - 입력 : 정수의 개수 N(1 <= N <= 100,000)
              이후 N개의 정수(-10,000 <= 정수 <= 10,000)
      - 출력 : 말해야 하는 수

    * 참고 : https://velog.io/@uoayop/BOJ-1655-%EA%B0%80%EC%9A%B4%EB%8D%B0%EB%A5%BC-%EB%A7%90%ED%95%B4%EC%9A%94Python
"""
from sys import stdin
import heapq

max_heap, min_heap = [], []
for _ in range(int(stdin.readline().strip())):
    x = int(stdin.readline().strip())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)

    if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0]*-1 > min_heap[0]:
        max_value = heapq.heappop(max_heap)*-1
        min_value = heapq.heappop(min_heap)

        heapq.heappush(max_heap, min_value*-1)
        heapq.heappush(min_heap, max_value)

    print(max_heap[0]*-1)
