"""
    문자열 뒤집기
     - 연결된 문자를 통으로 뒤집음, 뒤집어서 모든 숫자를 같게 만들어야 함
     - 입력 : 0과 1로 이루어진 문자열 S (S의 길이 <= 1,000,000)
     - 출력 : 행동의 최소 횟수
"""
from sys import stdin
s = stdin.readline().strip()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 모든 원소를 확인하며
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if s[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))