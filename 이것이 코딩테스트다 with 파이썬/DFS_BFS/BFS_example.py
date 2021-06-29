'''
    BFS
     1. 탐색 시작 노드를 큐에 삽입하고 방문처리
     2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
     3. 2의 과정을 수행할 수 없을 때까지 반복
    큐 기반 -> deque 라이브러리 사용 -> 일반적인 경우 실제 수행시간이 DFS보다 좋음
'''

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft() # 큐에서 하나의 원소를 pop
        print(v, end=' ')
        for i in graph[v]: # 해당 원소와 연결되었지만 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9 # 방문 정보

bfs(graph, 1, visited)