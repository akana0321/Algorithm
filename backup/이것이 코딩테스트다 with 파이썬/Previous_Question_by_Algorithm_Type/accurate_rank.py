"""
    정확한 순위
     - 입력 : 학생들의 수 N (2 <= N <= 500), 두 학생의 성적을 비교한 횟수 M(2 <= M <= 10,000)
             이후 A B가 주어지는데 A번 학생의 성적이 B번 학생보다 낮다는 것을 의미
     - 출력 : 성적 순위를 정확히 알 수 있는 학생이 몇 명인지 출력
"""
from sys import stdin

INF = int(1e9)

n, m = map(int, stdin.readline().split())
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    graph[a][b] = 1 # 연결이 있다는 표식

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)