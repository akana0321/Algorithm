"""
    최대 힙(https://www.acmicpc.net/problem/11279)
     - 다음과 같은 연산 지원
        1. 배열에 자연수 x를 넣는다
        2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다
     - 입력 : 연산의 개수 N(1 <= N <= 100,000)
             x가 0이면 가장 큰 값을 출력 후 제거, 아니면 배열에 추가
                입력되는 자연수는 2^31보다 작다
     - 출력 : 입력에서 0이 주어진 회수만큼 답을 출력

     ## 파이썬의 heapq는 최소힘이 default라 최대힙으로 사용하려면
        - 붙여서 저장한 후 절대값으로 빼주면 된다"""
from sys import stdin
import heapq

heap = []
for _ in range(int(stdin.readline().strip())):
    x = int(stdin.readline().strip())
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -x)
