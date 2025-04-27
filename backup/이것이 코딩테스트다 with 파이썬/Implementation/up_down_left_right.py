'''
    N X N 크기의 공간
    가장 왼쪽 위의 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N)
     L : 왼쪽으로 한 칸 이동
     R : 오른쪽으로 한 칸 이동
     U : 위로 한 칸 이동
     D : 아래로 한 칸 이동
    공간 밖을 넘어가는 경우에는 무시
     - 1 <= N <= 100
     - 1 <= 이동횟수 <= 100
     - 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력
'''

''' 내 풀이
n = int(input())
schedule = input().split()
start = [1, 1]

for word in schedule:
    if word == 'L' and start[0] != 1:
        start[0] -= 1
        print(start)
    elif word == 'R' and start[0] != n:
        start[0] += 1
        print(start)
    elif word == 'D' and start[1] != n:
        start[1] += 1
        print(start)
    elif word == 'U' and start[1] != 1:
        start[1] -= 1
        print(start)

print('%d %d' %(start[1], start[0]))
'''

# 다른 사람 풀이
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)