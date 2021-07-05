"""
    퀵 정렬
     - 기준 = 피벗(Pivot)을 기준으로 크고 작은 데이터의 위치를 바꿈
     - 여기서는 가장 대표적인 분할 방식인 호어 분할(Hoare Partition) 사용
     - 리스트에서 첫 번째 데이터를 피벗으로 설정, 왼쪽에서 피벗보다 큰 데이터를 찾고,
       오른쪽에서 피벗보다 작은 값을 찾음. 그리고 서로 교환
     - 위와 같은 과정이 끝나면 작은 쪽의 데이터들과 피벗의 위치를 바꿈
     - 이후 작은 데이터 셋들과 큰 데이터 셋들에서도 위와 같은 과정을 수행하여 정렬
     - 무작위로 데이터가 입력될 경우 빠르지만, 이미 정렬되어 있는 경우는 매우 느림
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 10, 8]


def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 그렇지 않다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort4python(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환
    return quick_sort4python(left_side) + [pivot] + quick_sort4python(right_side)


quick_sort(array, 0, len(array) - 1)
print(array)
print(quick_sort4python(array2))