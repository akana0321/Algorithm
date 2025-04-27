"""
    AC(https://www.acmicpc.net/problem/5430)
     - 함수는 R(뒤집기) D(버리기)
     - R은 배열에 있는 숫자의 순서를 뒤집는 함수고, D는 첫 번째 숫자를 버리는 함수.
        배열이 비어있는데 D를 사용한 경우에는 에러가 발생
     - 함수는 조합해서 사용이 가능
     - 입력 : 테스트 케이스의 개수 T(최대 100)
             수행할 함수 P(1 <= p의 길이 <= 100,000)
             배열에 들어있는 수의 개수 n(0 <= n <= 100,000)
             [x1, ....., xn]과 같은 형태로 배열에 들어있는 수가 주어짐(1 <= xi <= 100)
             전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않음
     - 출력 : 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력
              만약 에러가 발생한 경우에는 error을 출력
"""
from sys import stdin
from collections import deque

t = int(stdin.readline().strip())

for _ in range(t):
    p = list(stdin.readline().strip())
    n = int(stdin.readline().strip())
    data = stdin.readline()[1:-2].split(",")
    q = deque(data)

    rev, front, back = 0, 0, len(q) - 1
    flag = 0

    if n == 0:
        q = []
        front = 0
        back = 0

    for command in p:
        if command == 'R':
            rev += 1
        elif command == 'D':
            if len(q) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
