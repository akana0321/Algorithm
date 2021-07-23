"""
    감시 피하기(https://www.acmicpc.net/problem/18428)
     - 입력 : 복도의 크기 N(3 <= N <= 6)
             복도의 정보(학생은 S, 선생은 T, 아무것도 없으면 X)
     - 출력 : 정확히 3개의 장애물을 설치해서 감시를 피할 수 있다면 YES, 아니면 NO 출력
"""
from sys import stdin
from itertools import combinations

n = int(stdin.readline().strip())
hallway = []
spaces = []
teachers = []
for i in range(n):
    hallway.append(list(stdin.readline().split()))
    for j in range(n):
        if hallway[i][j] == 'X':
            spaces.append((i, j))
        if hallway[i][j] == 'T':
            teachers.append((i, j))

# 특정 방향으로 감시를 진행(학생 발견 시 True, 아니면 False)
def watch(x, y, direction):
    # 왼쪽 감시
    if direction == 0:
        while y >= 0:
            if hallway[x][y] == 'S':
                return True
            if hallway[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽 감시
    if direction == 1:
        while y < n:
            if hallway[x][y] == 'S':
                return True
            if hallway[x][y] == 'O':
                return False
            y += 1
    # 위쪽 감시
    if direction == 2:
        while x >= 0:
            if hallway[x][y] == 'S':
                return True
            if hallway[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽 감시
    if direction == 3:
        while x < n:
            if hallway[x][y] == 'S':
                return True
            if hallway[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        hallway[x][y] = 'O'
    # 학생이 한 명도 감지되지 않은 경우
    if not process():
        # 원하는 경우를 발견한 것
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        hallway[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")