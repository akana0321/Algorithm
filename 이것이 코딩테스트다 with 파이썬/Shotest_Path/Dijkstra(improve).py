"""
    개선된 다익스트라 알고리즘
     - 최악의 경우에도 시간 복잡도 O(ElogV)를 보장, V는 노드의 개수, E는 간선의 개수
     - Heap을 사용, 이를 이용하게 되면 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로 출발노드로부터 가장 거리가
       짧은 노드를 더욱 빠르게 찾을 수 있다
     - 큐와 우선순위 큐 : 데이터 삭제 시 큐는 먼저 삽입된 데이터, 우선순위 큐는 우선순위가 가장 높은 데이터를 삭제
     - 파이썬에서는 PriorityQueue와 heapq를 사용할 수 있는데 모두 우선순위 큐 기능을 지원, 하지만 heapq가 더 빠르므로 이를 택
     - 우선순위 큐 구현 시 최소 힙 or 최대 힙을 사용하는데 전자는 값이 낮은 데이터가 먼저 삭제, 후자는 값이 큰 데이터가 먼저 삭제
     - 파이썬에서는 기본적으로 최소 힙 구조를 이용 -> 가장 값이 작은 원소가 추출 -> 다익스트라에 적합
     - 최소 힙을 최대 힙처럼 사용하려면 -를 붙여서 저장하고, 데이터를 꺼낼 때 -를 붙여 보내면 됨
     - 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용한다고 보면 됨
     - simple 버전에서 만들었던 get_smallest_node() 함수를 만들 필요가 없음
     - 최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체할 수 있기 때문
"""
import heapq, sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 10억

# 노드, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 거내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])