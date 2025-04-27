"""
    고정점 찾기
     - 고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
     - 예를 들어, a = [-15, -4, 2, 8, 13]이 있을 때, a[2] = 2이므로 고정점은 2가 됨
     - 시간 복잡도 O(logN)으로 설계하지 않으면 시간 초과 판정
     - 입력 : N(1 <= N <= 1,000,000)
             N개의 원소(-10^9 <= 각 원소의 값 <= 10^9)
     - 출력 : 고정점, 없다면 -1
"""
from sys import stdin

# 이진 탐색 구현(재귀)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우
    else:
        return binary_search(array, mid + 1, end)

n = int(stdin.readline().strip())
array = list(map(int, stdin.readline().split()))

index = binary_search(array, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)