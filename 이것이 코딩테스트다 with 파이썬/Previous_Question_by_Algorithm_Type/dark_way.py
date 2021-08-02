"""
    어두운 길
     - 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 함
     - 입력 : 집의 수 N(1 <= N <= 200,000), 도로의 수 M(N - 1 <= M <= 200,000)
             X Y Z(0 <= X, Y < N), 이는 X번 집과 Y번 집 사이에 양방향 도로가 있으며 그 길이가 Z라는 뜻
              X, Y가 동일한 경우는 없으며, 마을을 구성하는 모든 도로의 길이 합은 2^31보다 작음
     - 출력 : 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액
"""
from sys import stdin

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, stdin.readline().split())
parent = [0] * n # 부모 테이블 초기화
for i in range(n):
    parent[i] = i

edges = [] # 모든 간선은 담는 리스트
sum_value = 0
result = 0 # 최소 cost

# 간선에 대한 정보 입력받기
for _ in range(m):
    x, y, cost = map(int, stdin.readline().split())
    # 비용 순으로 정렬해야 하기 때문에 첫번째 원소에 cost
    edges.append((cost, x, y))

edges.sort()

for edge in edges:
    cost, x, y = edge
    sum_value += cost
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(sum_value - result)