"""
    커리큘럼
     - 입력 : 듣고자 하는 강의의 수 N(1 <= N <= 500)
             다음 N개의 줄에는 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 주어짐(1 <= 강의시간 <= 100,000)
             강의의 번호는 1부터 N까지로 구성되며 각 줄은 -1로 끝남
     - 출력 : B개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력
"""
from sys import stdin
from collections import deque
import copy

# 노드의 개수 입력받기
v = int(stdin.readline().strip())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, stdin.readline().split()))
    time[i] = data[0] # 첫번째 수는 강의 시간이기 때문
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])

topology_sort()