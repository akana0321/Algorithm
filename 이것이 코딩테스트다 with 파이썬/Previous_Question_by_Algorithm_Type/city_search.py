"""
    특정 거리의 도시 찾기
     - 도로의 거리는 1
     - 입력 : 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
             (2 <= N <= 300,000, 1 <= M <= 1,000,000, 1 <= K <= 300,000, 1 <= X <= N)
             이후 M개의 줄에 걸쳐 A B 가 주어지는데, A번 도로에서 B번 도로로 이동이 가능하다는 뜻
     - 출력 : X 로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
             도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력
"""
from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# BFS
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시들을 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

print(distance)
# 최단거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단거리가 K인 도시가 없다면 -1 출력
if check == False:
    print(-1)