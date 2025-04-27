'''
    2667. 단지 번호 붙이기
'''
import sys


def dfs(x, y, cnt):
    dx = [-1, 1, 0, 0]
    dy = dx[::-1]
    arr[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or not arr[nx][ny]:
            continue
        cnt = dfs(nx, ny, cnt+1)
    return cnt


n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
cnt = 0
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans.append(dfs(i, j, 1))

print(len(ans))
for i in sorted(ans):
    print(i)
