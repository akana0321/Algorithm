"""
    탑승구
     - G개의 탑승구가 있으며, 각각의 탑승구는 1번부터 G번까지의 번호로 구분
     - P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 g(i)번째(1 <= g(i) <= G) 탑승구 중 하나에 영구 도킹
     - P개의 비행기를 순서대로 도킹하다 만약 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 공항 운행 중지
     - 입력 : 탑승구의 수 G(1 <= G <= 100,000)
             비행기의 수 P(1 <= P <= 100,000)
             비행기가 도킹할 수 있는 탑승구의 정보 g(i)(1 <= g(i) <= G), 이는 i번째 비행기가 1번부터 g(i)번째 탑승구 중
             하나에 도킹할 수 있다는 뜻
     - 출력 : 도킹할 수 있는 비행기의 최대 개수
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

g = int(stdin.readline().strip())
p = int(stdin.readline().strip())
parent = [0] * (g + 1) # 부모 테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구의 루트 확인
    if data == 0: # 현재 루트가 0이라면, 종료
        break
    union_parent(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)