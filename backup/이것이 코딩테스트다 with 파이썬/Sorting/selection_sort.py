"""
    선택 정렬
     - 데이터들 중에서 가장 원소를 찾아 맨 처음으로 보냄
     - 다음 두번째로 작은 원소를 찾아 두번째로 보냄.......
     - 비효율적이지만 특정 리스트에서 가장 작은 값을 찾는 일이 잦으므로 익숙해질 필요가 있음
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)