'''
    입력 받는 법 정리
'''

# 가장 기초적인 방법
a = input()
b = input().split()
c = map(int, input().split())

# 빠르게 입력받기 -> sys.stdin.readline()
from sys import stdin

# 하나의 정수 입력받기
d = int(stdin.readline().strip())

# 여러 개의 정수를 한 줄에 입력 받기
e, f, g = map(int, stdin.readline().split())

# 입력 받은 한 줄을 통으로 리스트에 저장
# ex) 1234 5678 -> [[1234], [5678]]
data = []
for i in range(d):
    data.append(list(map(int, stdin.readline().split())))

# 입력 받은 한 줄을 쪼개어 하나의 리스트에 저장
# ex) 1234 5678 -> [[1, 2, 3, 4], [5, 6, 7, 8]
newData = []
for i in range(d):
    newData.append(list(map(int, stdin.readline().strip())))