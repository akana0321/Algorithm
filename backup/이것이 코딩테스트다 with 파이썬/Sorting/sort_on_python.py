"""
    파이썬에서의 정렬
     - sorted() 함수를 제공
     - Merge Sort를 기반으로 만들어짐, 일반적으로 퀵 정렬보다는 느리지만 최악의 경우에도 O(NlogN)을 보장
     - sort나 sorted 함수에는 key 매개변수를 입력으로 받을 수 있는데, 이러한 경우 key를 기준으로 정렬하게 됨
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
result = sorted(array)
print(result)
array.sort()
print(array)

dic = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(dic, key=setting)
print(result)
print(dic[1])