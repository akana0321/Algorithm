"""
    모험가 길드
     - 입력 : 모험가의 수 N(1<+ N <= 100,000) / 공포도의 값을 N 이하의 자연수로 공백으로 구분하여 주어짐
     - 출력 : 여행을 떠날 수 있는 그룹 수의 최댓값
"""
from sys import stdin

n = int(stdin.readline().strip())
members = list(map(int, stdin.readline().split()))
members.sort()

result = 0 # 총 그룹의 수
group = 0 # 현재 그룹

for i in members:
    group += 1 # 현재 그룹에 해당 모험가 포함시키기
    if group >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면 그룹 결성
        result += 1 # 총 그룹의 수 증가 시키기
        group = 0 # 그룹 수 초기화

print(result)
