"""
    AC(https://www.acmicpc.net/problem/5430)
     - R은 뒤집기, D는 첫번째 숫자를 버리는 것
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

for _ in range(int(stdin.readline().strip())):
    cmds = stdin.readline().strip()
    n = int(stdin.readline().strip())
    ls = stdin.readline()[1:-2].split(',')
    q = deque(ls)
    reverse_count = 0

    for cmd in cmds:
        if cmd == 'R':
            reverse_count += 1
        else:
            if q: # <- 여기 손봐야됨
                if reverse_count % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                break

    if q:
        if reverse_count % 2 == 0:
            print('[' + ",".join(q) + ']')
        else:
            q.reverse()
            print('[' + ",".join(q) + ']')
    else:
        print("error")
