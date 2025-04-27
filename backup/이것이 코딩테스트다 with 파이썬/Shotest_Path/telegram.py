"""
    전보
     - 입력 : 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
             둘째줄부터 M + 1번 줄에 걸쳐 통로에 대한 정보인 X, Y, Z가 주어짐
             이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미
     - 출력 : 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력
"""
from sys import stdin
import heapq

INF = int(1e9)
n, m, c = map(int, stdin.readline().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)
# 그래프 정보 입력 받기
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    graph[x].append((y, z))

def dijkstar(start):
    q = []
    heapq.heappush(q, (0, start)) # (거리, 시작노드)
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

dijkstar(c)

count = 0
max_visited = 0
for d in distance:
    if d != INF:
        count += 1
        max_visited = max(max_visited, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_visited)