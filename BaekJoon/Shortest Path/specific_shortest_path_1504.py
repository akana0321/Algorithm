"""
    특정한 최단 경로(https://www.acmicpc.net/problem/1504)
     - 방향성이 없는 그래프, 1번에서 N번 정점으로 가는 최단 거리
     - 임의로 주어진 두 정점은 반드시 통과해야 함
     - 한 번 이동했던 정점, 한 번 이동했던 간선도 다시 이용 가능하지만 반드시 최단 경로로 이동해야 함
     - 입력 : 정점의 개수 N, 간선의 개수 E(2 <= N <= 800, 0 <= E <= 200,000)
             a b c가 주어지는데, a에서 b로 가는 양방향 길이 존재하며 그 길이 c라는 뜻(1 <= c <= 1,000)
             다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1, v2(v1 != v2, v1 != N, v2 != 1)
     - 출력 : 두 개의 정점을 지나는 최단 경로의 길이 출력, 없을 경우 -1 출력
"""
from sys import stdin
import heapq
INF = int(1e9)


def dijkstra(start, end):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]


n, e = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, stdin.readline().split())

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)


if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))
