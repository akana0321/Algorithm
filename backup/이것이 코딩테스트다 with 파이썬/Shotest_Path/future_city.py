"""
    미래도시
     - 입력 : 전체 회사의 개수 N(N>=1), 경로의 개수 M(M<=100) / M + 1번째 줄까지 연결된 두 회사의 번호가 공백으로 구분되어 입력
             M + 2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어짐
     - 출력 : K를 거쳐 X로 가는 최소 이동 시간을 출력
             만약 X에 도착할 수 없다면 -1을 출력
     * A는 1에서 시작임
"""
from sys import stdin

INF = int(1e9)

n, m = map(int, stdin.readline().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, stdin.readline().split())

# Floyd_Warshall
def floyd_warshall(vertex, graph):
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

floyd_warshall(n, graph)

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1을 출력
if distance >= INF:
    print("-1")
else:
    print(distance)
