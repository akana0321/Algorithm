"""
    숨바꼭질
     - 1 ~ N번 까지의 방 중 하나에 숨음, 술래는 1번 방부터 시작
     - 전체 맵에는 M개의 양방향 통로가 존재, 하나의 통로는 서로 다른 두 방을 연결
     - 최단 거리가 가장 먼 방, 최단 거리의 의미는 지나야 하는 길이 최소 개수를 의미
     - 입력 : n m (2 <= N <= 20,000, 1 <= M <= 50,000)
             이후 서로 연결된 방 A B
     - 출력 : 숨어야 하는 방 번호(여러 개면 가장 작은 번호)  방까지의 거리  그 방과 같은 거리를 갖는 방의 수
"""
from sys import stdin
import heapq
INF = int(1e9)

n, m = map(int, stdin.readline().split())
start = 1 # 시작점
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 최단 거리가 가장 먼 노드 번호
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))

