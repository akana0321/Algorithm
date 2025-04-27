"""
    단어 공부(https://www.acmicpc.net/problem/1157)
     - 알파벳 대소문자로 된 단어가 주어지만, 이 단어에서 가장 많이 사용된 알파벳이 ㅁ엇인지를
       알아내는 프로그램, 대소문자 구별 안함
     - 입력 : 대소문자로 이루어진 단어, 길이는 1,000,000을 넘지 않는다
     - 출력 : 가장 많이 사용된 알파벳을 대문자로 출력
             단 가장 많이 사용된 알파벳이 여러개 존재하는 경우에는 ? 출력
"""
from sys import stdin

s = str(stdin.readline())
convert_s = s.upper()

alpha_list = []
for i in range(ord('A'), ord('Z') + 1):
    alpha_list.append(convert_s.count(chr(i)))

maxNum = max(alpha_list)
if alpha_list.count(maxNum) == 1:
    alphabet = chr(alpha_list.index(maxNum) + 65)
    print(alphabet)
else:
    print('?')