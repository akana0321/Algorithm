"""
    문자열 재정렬
     - 입력 : 알파벳 대문자와 0 ~ 9 의 숫자
     - 출력 : 정렬한 알파벳 + 모든 숫자의 합
"""
from sys import stdin
import copy

s = list(stdin.readline().strip())
s.sort()
temp = copy.deepcopy(s)
sum_value = 0

for i in range(0, len(temp)):
    if ord('0') <= ord(temp[i]) <= ord('9'):
        sum_value += int(temp[i])
        s.remove(temp[i])
    else:
        break

s.append(str(sum_value))
print("".join(s))