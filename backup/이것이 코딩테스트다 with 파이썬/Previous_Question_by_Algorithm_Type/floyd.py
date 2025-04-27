"""
    플로이드(https://www.acmicpc.net/problem/11404)
     - 입력 : 도시의 개수 n (1 <= n <= 1000)
             버스의 개수 m (1 <= m <= 100,000)
             이후 버스의 정보 a(시작) b(도착) c(비용) 순으로 주어짐, 비용은 100,000 보다 작거나 같음
             시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수도 있다
     - 출력 : n개의 줄을 출력해야 함. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는 데 필요한 최소 비용
             만약, i에서 j로 갈 수 없다면 그 자리에 0을 출력
"""
from sys import stdin

INF = int(1e9)

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    graph[i][i] = 0 # 자기 자신으로 가는 것은 초기화

for _ in range(m):
     a, b, c = map(int, stdin.readline().split())
     if c < graph[a][b]:
         graph[a][b] = c

# 플로이드 워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없다면 0 출력
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()