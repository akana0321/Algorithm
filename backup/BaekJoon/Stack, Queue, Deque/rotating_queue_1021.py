"""
    회전하는 큐(https://www.acmicpc.net/problem/1021)
     - 3가지 연산
        * 첫 번째 원소를 뽑아낸다
        * 첫 번째 원소를 뒤로 보냄
        * 마지막 원소를 맨 앞으로 보냄
     - 뽑아내려고 하는 수를 주어진 순서대로 뽑아내는데 드는 2, 3번 연산의 최솟값 출력
     - 입력 : 큐의 크기 N 뽑아내려고 하는 수의 개수 M
                N은 50보다 작거나 같은 자연수, M은 N보다 작거나 같은 자연수
             이후 뽑아내려고 하는 수의 위치가 순서대로 주어짐
                위치는 1보다 크거나 같고, N보다 작거나 같은 자연수
     - 출력 : 답
"""
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
targets = list(map(int, stdin.readline().split()))
dq = deque([i for i in range(1, n+1)])

count = 0
for target in targets:
    while True:
        if dq[0] == target:
            dq.popleft()
            break
        else:
            if dq.index(target) < len(dq)/2:
                while dq[0] != target:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != target:
                    dq.appendleft(dq.pop())
                    count += 1

print(count)
