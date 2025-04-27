"""
    카드2(https://www.acmicpc.net/problem/2164)
     - 1 ~ N까지의 숫자들
     - 제일 위의 카드를 버리고, 그 다음 카드를 맨뒤로 -> 한 장 남을 때까지 반복
     - 입력 : 정수 N(1 <= N <= 500,000)
     - 출력 : 남게 되는 카드의 번호
"""
from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
cards = [i for i in range(1, n+1)]
q = deque(cards)
count = 0

while len(q) > 1:
    if count % 2 == 0:
        q.popleft()
        count += 1
    else:
        q.append(q.popleft())
        count += 1

print(q.pop())