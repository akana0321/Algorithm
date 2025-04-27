"""
    두 수 비교하기(http://acmicpc.net/problem/1330)
     - 입력 : A, B(-10,000 <= A, B <= 10,000)
     - 출력 : A가 B보다 크면 >
                 "    작으면 <
                 "    같으면 ==

"""
from sys import stdin

a, b = map(int, stdin.readline().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print("==")