"""
    덱(https://www.acmicpc.net/problem/10866)
     - 덱의 기능 8가지
        * push_front X: 정수 X를 덱의 앞에 넣는다.
        * push_back X: 정수 X를 덱의 뒤에 넣는다.
        * pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        * pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        * size: 덱에 들어있는 정수의 개수를 출력한다.
        * empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
        * front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        * back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     - 입력 : 명령의 수 N(1 <= <= 10,000)
              N개의 명령, 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다
"""
from sys import stdin
from collections import deque

q = deque()

for _ in range(int(stdin.readline().strip())):
    command = stdin.readline().split()

    if command[0] == "push_front":
        q.appendleft(command[1])
    elif command[0] == "push_back":
        q.append(command[1])
    elif command[0] == "pop_front":
        if q:
            temp = q.popleft()
            print(temp)
        else:
            print(-1)
    elif command[0] == "pop_back":
        if q:
            temp = q.pop()
            print(temp)
        else:
            print(-1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(0 if q else 1)
    elif command[0] == "front":
        print(q[0] if q else -1)
    elif command[0] == "back":
        print(q[-1] if q else -1)