"""
    ACM 호텔(https://www.acmicpc.net/problem/10250)
     - 호텔은 높이 H, 한 층당 방의 수 W로 구성되어 있고
       손님들은 정문에서 가까운 쪽으로 배치되는 것을 선호
       엘레베이터로 이동하는 거리는 신경 쓰지 않음
     - 입력 : 테스트 케이스의 횟수 t
             H(호텔의 층 수) W(각 층의 방 수) N(몇번째 손님인지) (1 <= H, W <= 99, 1 <= N <= H x W)
     - 출력 : 각 테스트 데이터마다 N 번째 손님에게 배정되어야 하는 방 번호
"""
from sys import stdin

for _ in range(int(stdin.readline())):
    H, W, N = map(int, stdin.readline().split())

    level = N % H
    line = N // H + 1

    if level == 0:
        level = H
        line -= 1

    print(level * 100 + line)
