"""
    토마토(https://www.acmicpc.net/problem/7576)
     - 입력 : 상자의 크기를 나타내는 두 정수 M N
                M은 가로, N은 세로(2 <= M, N <= 1,000)
             이후 토마토들의 정보, 1은 익은 토마토, 0 은 익지 않은 토마토, -1은 토마토가 없는 칸
             토마토가 하나 이상 있는 경우만 입력으로 주어짐
     - 출력 : 토마토가 모두 익을 때까지의 최소 날짜를 출력
             만약, 저장될 때부터 모든 토마토가 익어있는 상태면 0을 출력, 모두 익지 못하는 상황이면 -1을 출력
"""
from sys import stdin
from collections import deque


# 익은 토마토를 deque에 넣기
def checkRipe(n, m, graph):
    dq = deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dq.append([i, j])
    return dq


# BFS 알고리즘
def bfs(n, m, graph):
    global ripeDq
    dx = [-1, 0, 1, 0]
    dy = dx[::-1]
    count = 1 # 출력용 카운트1

    while ripeDq:
        x, y = ripeDq.popleft()
        count2 = 0 # 출력용 카운트2
        for i in range(4):
            count2 += 1
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                ripeDq.append([nx, ny])
                """ 출력용 문단 """
                for ele in box:
                    print(ele)
                print("------------***{}-{}***--------------\n".format(count, count2))
        count += 1


# 결과 출력
def print_result(graph, result):
    for i in graph:
        for j in i:
            if j == 0:
                print(-1)
                return
        result = max(result, max(i))
    print(result-1) # 익은 토마토(1)에 갯수를 더해가므로 마지막에 1을 빼야함
    return


m, n = map(int, stdin.readline().split())
box = [list(map(int, stdin.readline().split())) for _ in range(n)]
res = 0

ripeDq = checkRipe(n, m, box)
bfs(n, m, box)
print_result(box, res)

for i in box:
    print(i)

