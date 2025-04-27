"""
    드래곤 커브(https://www.acmicpc.net/problem/15685)

    * 참고 : https://kyun2da.github.io/2021/04/06/dragonCurve/
"""
from sys import stdin

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
n = int(stdin.readline().strip())
# 드래콘 커브들이 모일 배열, 1이면 드래곤 커브의 일부
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    # x, y : 드래곤 커브의 시작점, d : 시작 방향, g : 세대
    x, y, d, g = map(int, stdin.readline().split())
    arr[x][y] = 1

    move = [d]
    # g 세대 만큼 반복
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i - 1] + 1) % 4)
        move.extend(temp)

    # 드래곤 커브에 해당하는 좌표를 arr에 추가
    for i in move:
        nx, ny = x + dx[i], y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

# 모든 꼭짓점이 드래곤 커브의 일부인 정사각형의 개수 구하기
result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            result += 1

print(result)
