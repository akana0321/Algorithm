"""
    미확인 도착지(https://www.acmicpc.net/problem/9370)
     - 입력 : 테스트 케이스의 개수 T(1 <= T <= 100)
             첫번째 줄에 3개의 정수 n, m, t(2 <= n <= 2,000, 1 <= m <= 50,000, 1 <= 1t <= 100)
                각각 교차로, 도로, 목적지 후보의 개수
             두번째 줄에 3개의 정수 s, g, h(1 <= s, g, h <= n)
                s는 예술가들의 출발지, g, h는 지나간 교차로의 사이(g != h)
             이후 m개의 각 줄마다 3개의 정수 a, b, d(1 <= a < b <= n, 1 <\ d <= 1,000)
                a와 b사이에 길이 d의 양방향 도로가 있다는 뜻
             이후 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미
                이 t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않음
             교차로 사이에는 도로가 많아봐야 1개, m개의 줄 중에서 g와 h 사이의 도로를 나타낸 것이 존재
                또한 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부
     - 출력 : 각 테스트 케이스마다 입력에서 주어진 목적지 후보들 중 불가능한 경우를 제외한 목적지들을 공백으로 분리시킨
                오름차순의 정수들로 출력

     * 참고 : https://hooongs.tistory.com/165
"""
from sys import stdin
import heapq

INF = float(1e9)


def dijkstra(n, start, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


for _ in range(int(stdin.readline().strip())):
    n, m, t = map(int, stdin.readline().split())
    s, g, h = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, stdin.readline().split())
        if (a == g and b == h) or (a == h and b == g):
            d -= 0.1 # h, g 사이의 거리
        graph[a].append((b, d))
        graph[b].append((a, d))
    targets = [int(stdin.readline().strip()) for _ in range(t)]
    targets.sort()

    dijkstra_results = dijkstra(n, s, graph)

    for target in targets:
        if dijkstra_results[target] != INF and type(dijkstra_results[target]) == float:
            print(target, end=' ')
    print()
