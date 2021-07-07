"""
    이진 탐색
     - 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있음
     - 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
     - 사용하는 경우가 많으니 외워두는 것이 좋다
     - loop로 구현한게 짧으니 외우기 쉬울 것 같음
"""
from sys import stdin


def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 target이 작은 경우 왼쪽으로
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    # 중간점의 값보다 target이 크면 오른쪽으로
    else:
        return binary_search_recursive(array, target, mid + 1, end)

def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def answer(result):
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print("%d번째에 위치하고 있습니다" % (result + 1))

# 원소의 개수 n과 찾고자 하는 문자열 target을 입력 받기
n, target = list(map(int, stdin.readline().split()))
# 전체 원소 입력 받기
array = list(map(int, stdin.readline().split()))

answer(binary_search_recursive(array, target, 0, n - 1))
answer(binary_search_loop(array, target, 0, n - 1))