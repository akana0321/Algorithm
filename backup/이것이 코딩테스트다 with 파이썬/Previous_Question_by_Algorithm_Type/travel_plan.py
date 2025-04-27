"""
    여행 계획
     - 입력 : 여행지의 수 N, 여행 계획에 속한 도시의 수 M (1 <= N, M <= 500)
             N X N 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부가 주어짐
              값이 1이라면 서로 연결되었다는 의미, 0이라면 서로 연결되어 있지 않다는 의미
             마지막 줄에 여행 계획에 포함된 여행지의 번호들이 주어지며 공백으로 구분
     - 출력 : 여행 계획이 가능하다면 YES, 아니면 NO 출력
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

n, m = map(int, stdin.readline().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(n):
    data = list(map(int, stdin.readline().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우 union 연산 수행
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plan = list(map(int, stdin.readline().split()))

result = True
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

print("YES" if result else "NO")
