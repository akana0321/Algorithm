"""
    행성 터널(https://www.acmicpc.net/problem/2887)
     - 입력 : 행성의 개수 N (1 <= N <= 100,000)
             각 행성의 x, y, z 좌표
             모든 좌표 값은 -10^9보다 크거나 같고, 10^9보다 작거나 같다
             한 위치에 행성이 두 개 이상 잇는 경우는 없음
     - 출력 : 모든 행성을 터널로 연결하는데 필요한 최소 비용
"""
from sys import stdin

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(stdin.readline().strip())
parent = [0] * (n + 1) # 부모 테이블 초기화
for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

x = []
y = []
z = []

# 모든 노드에 대한 좌표값 입력받기
for i in range(1, n + 1):
    data = list(map(int, stdin.readline().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)