"""
    최종 순위(https://www.acmicpc.net/problem/3665)
     - 입력 : 테스트 케이스의 개수, 100개를 넘지 않음. 각 테스트 케이스는 다음과 같이 이루어져 있음
              - 팀의 수 n을 포함하고 있는 한 줄(2 <= n <= 500)
              - n개의 정수 t(i)를 포함하고 있는 한 줄(1 <= t(i) <= n), t(i)는 작년에 i등을 한 팀의 번호
                1등이 가장 성적이 높은 팀이며 모든 t(i)는 서로 다름
              - 상대적인 등수가 바뀐 쌍의 수 m(0 <= m <= 25000)
              - 두 정수 a(i)와 b(i)를 포함하고 있는 m줄(1 <= a(i) < b(i) <= n) 상대적인 등수가 바뀐 두 팀이 주어짐
                같은 쌍이 여러 번 발표되는 경우는 없음
     - 출력 : 각 테스트 케이스에 대해서 다음을 출력
              - n개의 정수를 한 줄에 출력. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력
                만약 확실한 순위를 찾을 수 없다면 "?"을 출력
                데이터에 일관성이 없어서 순위를 정할 수 없는 경우 "IMPOSSIBLE"을 출력
"""
from sys import stdin
from collections import deque

for tc in range(int(stdin.readline().strip())):
    n = int(stdin.readline().strip())   # 노드 개수
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    data = list(map(int, stdin.readline().split())) # 작년 순위 정보
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    m = int(stdin.readline().strip()) # 올해 변경된 순위 정보
    for i in range(m):
        a, b = map(int, stdin.readline().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 쿠 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False # 그래프 내에 사이클이 존재하는지 여부

    # 정확히 노드의 개수만큼 반복
    for i in  range(n):
        # 큐가 비어있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생하는 경우(일관성이 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif not certain:
        print("?")
    # 위상 정렬을 수행한 결과 추 ㄹ력
    else:
        for i in result:
            print(i, end=' ')
        print()