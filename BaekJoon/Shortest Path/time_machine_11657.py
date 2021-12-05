"""
    타임머신(https://www.acmicpc.net/problem/11657)
     - N개의 도시, M개의 버스
     - 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 걸리는 시간
     - C가 양수가 아닌 경우가 있는데, 0은 순간이동, 음수는 타임머신으로 시간을 되돌아가는 경우
     - 입력 : 도시의 개수 N(1 <= N <= 500), 버스 노선의 개수 M(1 <= M <= 6,000)
             이후 버스 노선의 정보 A B C(1 <= A, B <= N, -10,000 <= C <= 10,000)
     - 출력 : 1번 도시에서 다른 도시로 가는데 걸리는 시간
             어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 -1을 출력
             해당 도시로 가는 경로가 없을 때도 -1을 출력
"""
from sys import stdin
INF = float(1e9)


def bellman_ford(n, m, start, graph, distance):
    distance[start] = 0

    for i in range(1, n + 1):
        for j in range(m):
            now, next, cost = graph[j][0], graph[j][1], graph[j][2]
            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                if i == n:
                    return True
    return False


n, m = map(int, stdin.readline().split())
graph = []
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph.append((a, b, c))

negative_cycle = bellman_ford(n, m, 1, graph, distance)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        # 도달할 수 없는 경우
        if distance[i] == INF:
            print(-1)
        # 도달 가능한 경우
        else:
            print(distance[i])
