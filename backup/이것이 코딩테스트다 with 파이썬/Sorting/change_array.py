"""
    두 배열의 원소 교체
     - 두 개의 배열이 주어짐, 첫번째 배열의 원소합이 최대가 되도록 두번째 배열과 교환
     - 입력 : 원소 갯수 n, 바꿀 수 있는 횟수 k
     - 출력 : 첫번재 배열의 합
"""
from sys import stdin

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:   # a의 원소가 b의 원소보다 크거나 같을 때는 더이상 비교할 필요가 없으므로 탈출
        break

print(sum(a))
