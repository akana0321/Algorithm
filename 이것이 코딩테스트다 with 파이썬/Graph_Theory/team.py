"""
    팀 결성
     - 입력 : 학생 수 N, 연산의  개수 M
             다음 M개의 줄에는 각각의 연산이 주어짐
              1. 팀 합치기 연산은 0 a b 형태로 주어지는데 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 뜻
              2. 같은 팀 여부 확인 연산은 1 a b 형태로 주어지는데 이는 a번 학생과 b번 학생이 같은 팀에 속해있는지 확인하는 연산
             a와 b는 N 이하의 양의 정수이다
     - 출력 : 같은 님 여부 확인 연산에 대하여 한 줄에 하나씩 YES or NO로 결과를 출력한다
"""
from sys import stdin

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
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

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, stdin.readline().split())
    # 합집합 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
print()
print(parent)