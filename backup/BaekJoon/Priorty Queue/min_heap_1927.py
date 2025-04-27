"""
    최소 힙(https://www.acmicpc.net/problem/1927)
     - 입력 : 연산의 개수 N(1 <= N <= 100,000)
             0이면 가장 작은 값을 출력하고 제거, 아니면 배열에 추가
                입력되는 숫자는 2^31보다 작은 자연수 또는 0
     - 출력 : 0이 주어진 횟수만큼 답을 출력
"""
from sys import stdin
import heapq

heap = []
for _ in range(int(stdin.readline().strip())):
    x = int(stdin.readline().strip())
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
