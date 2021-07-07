"""
    순차 탐색
     - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 순차적으로 찾는 방식
"""
from sys import stdin

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1 # 순번 반환(인덱스는 0부터 시작이므로 1을 더함)


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = stdin.readline().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다")
array = stdin.readline().split()

print(sequential_search(n, target, array))
print(array)