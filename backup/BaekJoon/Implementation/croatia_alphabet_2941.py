"""
    크로아티아 알파벳(https://www.acmicpc.net/problem/2941)
     - 입력 : 최대 100글자의 단어, 앒파벳 소문자와 -, = 로만 이루어져 있음
     - 출력 : 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
"""
from sys import stdin

words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

voca = stdin.readline().strip()

for word in words:
    if word in voca:
        voca = voca.replace(word, " ")

print(len(voca))
