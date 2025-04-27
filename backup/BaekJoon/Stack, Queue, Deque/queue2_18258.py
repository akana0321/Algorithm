"""
    큐 2(https://www.acmicpc.net/problem/18258)
     - 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리
     - 명령은 총 여섯 가지
        * push X: 정수 X를 큐에 넣는 연산이다.
        * pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        * size: 큐에 들어있는 정수의 개수를 출력한다.
        * empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        * front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        * back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     - 입력 : 명령의 수 N (1 <= N <= 2,000,000)
             이후 명령, 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다
     - 출력 : 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
"""
from sys import stdin
from collections import deque

q = deque()
count = 0

for _ in range(int(stdin.readline().strip())):
    command = stdin.readline().split()
    if command[0] == "pop":
        if q:
            temp = q.popleft()
            count -= 1
            print(temp)
        else:
            print(-1)
    elif command[0] == "push":
        num = int(command[-1])
        count += 1
        q.append(num)
    elif command[0] == "back":
        print(q[-1] if q else -1)
    elif command[0] == "size":
        print(count)
    elif command[0] == "front":
        print(q[0] if q else -1)
    elif command[0] == "empty":
        print(0 if q else 1)
