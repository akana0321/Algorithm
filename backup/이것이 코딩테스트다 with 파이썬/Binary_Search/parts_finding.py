"""
    부품 찾기
     - 입력 : 부품의 개수 n / n개의 부품 / 손님이 찾으려는 부품의 수 m / m개의 부품
     - 출력 : m개의 부품이 있는지 없는지를 판단하여 yes or no 로 출력
"""
from sys import stdin

n = int(stdin.readline().rstrip())
products = list(map(int, stdin.readline().split()))
m = int(stdin.readline().rstrip())
seek = list(map(int, stdin.readline().split()))

print("나의 풀이")
for ele in seek:
    if products.count(ele) != 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')

print("\n\n이진 탐색 풀이")
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in seek:
    result = binary_search(products, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print("\n\n계수 정렬 풀이(입력부터 다시 해야 함)")
N = int(stdin.readline().rstrip())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in stdin.readline().split():
    array[int(i)] = 1

M = int(stdin.readline().rstrip())
x = list(map(int, stdin.readline().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print("\n\n집합 자료형 이용(제품 목록 배열만 입력, 위의 n, m, x 재사용)")
array = set(map(int, stdin.readline().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')