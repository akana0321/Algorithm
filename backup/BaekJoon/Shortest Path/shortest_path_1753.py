"""
    최단경로(https://www.acmicpc.net/problem/1753)
     - 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 결로를 구하는 프로그램
        단, 모든 간선의 가중치는 10 이하의 자연수
     - 입력 : 정점의 개수 V, 간선의 개수 E(1 <= V <= 20,000, 1 <= E <= 300,000)
                모든 정점에는 1부터 V까지의 번호가 매겨져 있다고 가정
             두번째 줄에는 시작 정점의 번호 K(1 <= K <= V)
             세번째 줄 부터는 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수(u, v, w)가 순서대로 주어짐
                이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻
                u와 v는 서로 다르며 w는 10 이하의 자연수
                서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있다
     - 출력 : V개의 줄에 걸쳐, i번째 줄에 i번 정점으로 최단 경로의 경로값을 출력한다
"""
from sys import stdin
import heapq
INF = int(1e9)


def dijkstra(start):
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


v, e = map(int, stdin.readline().split())
k = int(stdin.readline().strip())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))

dijkstra(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

