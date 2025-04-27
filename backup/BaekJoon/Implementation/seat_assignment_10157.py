"""
    자리배정(https://www.acmicpc.net/problem/10157)

"""
from sys import stdin
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

c, r = map(int, stdin.readline().split())
k = int(stdin.readline())
graph = [[0] * r for _ in range(c)]
graph[0][0] = 1

q = [[0, 0]]
dir = 0
while q:
    x, y = q.pop()
    if graph[x][y] == k:
        print(x+1, y+1)
        exit()

    nx, ny = x+dx[dir], y+dy[dir]
    if 0 <= nx < c and 0 <= ny < r and not graph[nx][ny]:
        graph[nx][ny] = graph[x][y] + 1
        q.append([nx, ny])
    else:
        dir = (dir+1)%4
        nx, ny = x+dx[dir], y+dy[dir]
        if 0 <= nx < c and 0 <= ny < r and not graph[nx][ny]:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx, ny])

print(0)
