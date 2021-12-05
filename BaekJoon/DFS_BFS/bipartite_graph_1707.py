"""
    이분 그래프(https://www.acmicpc.net/problem/1707)
     - 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
        그러한 그래프를 특별히 이분 그래프라 부른다
        그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별
     - 입력 : 테스트 케이스의 개수 K(2 <= K <= 5)
             정점의 개수 V 간선의 개수 E(1 <= V <= 20,000, 1 <= E <= 200,000)
                각 정점에는 1부터 V까지 차례로 번호가 붙어있다
             이후 E개의 줄에 걸쳐 간선에 대한 정보, 각 줄에 인접한 두 정점의 번호 u, v(u != v)가 주어짐
     - 출력 : K개의 줄에 걸쳐 이분 그래프이면 YES, 아니면 NO를 순서대로 출력

     * 참고 : https://vixxcode.tistory.com/24
"""
from sys import stdin
from collections import deque


def bfs(v, e, graph, start):
    global visited
    visited[start] = 1
    dq = deque()
    dq.append(start)

    while dq:
        now = dq.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = -visited[now]
                dq.append(i)
            else:
                if visited[i] == visited[now]:
                    return False
    return True


def isTrue(v, e, graph):
    global visited
    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(v, e, graph, i):
                return False
    return True


for _ in range(int(stdin.readline().strip())):
    v, e = map(int, stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    print("YES" if isTrue(v, e, graph) else "NO")
