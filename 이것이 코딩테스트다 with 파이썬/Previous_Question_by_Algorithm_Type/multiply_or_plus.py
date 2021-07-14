"""
    곱하기 혹은 더하기
     - 입력 : 여러개의 숫자로 구성된 하나의 문자열 S(1 <= S의 길이 <= 20)
     - 출력 : 만들어질 수 있는 가장 큰 수
"""
from sys import stdin
s = list(map(int, stdin.readline().strip()))

result = 0

for ele in s:
    if result == 0:
        result += ele
    else:
        result *= ele

print(result)