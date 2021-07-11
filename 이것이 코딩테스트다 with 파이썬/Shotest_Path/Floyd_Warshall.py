"""
    플로이드 워셜 알고리즘
     - 다익스트라의 경우는 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우에 사용
     - 플로이드 워셜은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용
     - 단계마다 거쳐가는 조드를 기준으로 알고리즘을 수행, 하지만 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없음
     - 노드의 개수가 N개일 대 알고리즘상 N번의 단계를 수행, 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려
       -> 총시간 복잡도는 O(N^3)
     - 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보를 담아야 하기 때문에 2차원 리스트에 최단 거리 정보를 저장해야 함
     - 다익스트라는 그리디, 플로이드 워셜은 다이나믹 프로그래밍
       -> 노드의 개수가 N일 때, N번 만큼의 단계를 반복하여 점화식에 맞게 2차원 리스트를 갱신하기 때문
"""
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우 무한(INFINITY) 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()