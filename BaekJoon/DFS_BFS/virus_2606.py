'''
    2606. 바이러스
'''
from collections import deque

n = int(input())
edge = int(input())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(edge):
    e1, e2 = map(int, input().split())
    matrix[e1][e2] = matrix[e2][e1] = 1


def bfs(n, matrix):
    queue = deque([1])
    visited = [1]
    while queue:
        current = queue.popleft()
        for i in range(n + 1):
            if matrix[current][i] and i not in visited:
                queue.append(i)
                visited.append(i)
    return visited


print(len(bfs(n, matrix)) - 1) # 0을 빼줘야 함