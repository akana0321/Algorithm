'''
    DFS
     1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
     2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리
        방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
     3. 2의 과정을 수행할 수 없을 때까지 반복
'''

def dfs(graph, v, visited): # v는 시작노드
    visited[v] = True # 현재 노드 방문처리
    print(v, end=' ')
    # 인접 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)