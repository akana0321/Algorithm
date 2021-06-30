'''
    1260. DFS와 BFS
     - 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
     - 더 이상 방문할 수 있는 점이 없다면 종료
     - 정점의 개수 N, 간선의 개수 M, 시작할 정점의 번호 V
     - 방문한 순서대로 출력
'''

from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)] # n + 1 하는 이유는 인덱스가 0번부터여서 맞추기 위해
'''
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]] 
'''
for _ in range(m):
    e1, e2 = list(map(int, input().split()))
    matrix[e1][e2] = matrix[e2][e1] = 1
'''
     0  1  2  3  4
0  [[0, 0, 0, 0, 0],
1   [0, 0, 1, 1, 1],
2   [0, 1, 0, 0, 0],
3   [0, 1, 0, 0, 1],
4   [0, 1, 1, 1, 0]]
'''


def dfs(v, visited, matrix):
    visited.append(v)
    for i in range(1, n + 1):
        if matrix[v][i] and i not in visited:
            visited = dfs(i, visited, matrix)
    return visited


def bfs(v, matrix):
    queue = deque([v])
    visited = [v]
    while queue:
        current = queue.popleft()
        for i in range(1, n + 1):
            if matrix[current][i] and i not in visited:
                queue.append(i)
                visited.append(i)
    return visited


print(*dfs(v, [], matrix))
print(*bfs(v, matrix))