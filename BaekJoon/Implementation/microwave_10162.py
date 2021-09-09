"""
    전자레인지(https://www.acmicpc.net/problem/10162)
     - A B C 버튼 각각 5분 1분 10초
     - 세 버튼으로 해결할 수 있으면 각 횟수를, 안되면 -1 출력
     - 입력 : 요리시간 T(1 <= T <= 10,000)
     - 출력 : 최소 버튼 조작의 A B C 횟수
                해당 버튼을 누르지 않는 경우에는 0을 출력
                3개의 버튼으로 T초를 맞출 수 없으면 -1을 출력
"""
from sys import stdin

t = int(stdin.readline().strip())
button = [0, 0, 0]

if t % 10 != 0:
    print(-1)
else:
    while t > 0:
        if t // 300 != 0:
            button[0] = t // 300
            t %= 300
            continue
        elif t // 60 != 0:
            button[1] = t // 60
            t %= 60
            continue
        elif t // 10 != 0:
            button[2] = t // 10
            t = -1
            break
    print(*button)