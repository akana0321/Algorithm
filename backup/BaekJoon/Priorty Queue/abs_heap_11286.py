"""
    절대값 힙(https://www.acmicpc.net/problem/11286)
     - 다음과 같은 연산 지원
        1. 배열에 정수 x(x!=0)을 넣는다
        2. 배열에서 절댓값이 가장 작은 값을 출력 후 제거, 절댓값이 가장 작은 값이 여러개 일때는
            가장 작은 수를 출력하고, 그 값을 배열에서 제거
      - 입력 : 연산의 개수 N(1 <= N <= 100,000)
                x가 0이면 절댓값이 가장 작은 값을 출력 후 제거, 아니면 배열에 추가
                입력되는 정수는 -2^31보다 크고, 2^31보다 작다
     - 출력 : 입력에서 0이 주어진 회수만큼 답을 출력
"""
from sys import stdin
import heapq

heap = []

for _ in range(int(stdin.readline().strip())):
    x = int(stdin.readline().strip())

    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        element = heapq.heappop(heap)
        print(element[1])
    else:
        heapq.heappush(heap, [abs(x), x])
