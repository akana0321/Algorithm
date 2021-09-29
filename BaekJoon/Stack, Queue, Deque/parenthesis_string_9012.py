"""
    괄호(https://www.acmicpc.net/problem/9012)
     -  괄호 열고 닫고가 쌍으로 존재 = VPS
     - 입력 : 테스트케이스의 수 T
             이후 문자열(2이상 50이하의 길이)
     - 출력 : 각 테스트케이스마다 VPS면 YES, 아니면 NO를 출력
"""
""" 첫 풀이
from sys import stdin

for _ in range(int(stdin.readline().strip())):
    sts = stdin.readline().strip()
    stack = []
    flag = True
    for st in sts:
        if st == '(':
            stack.append(st)
        elif st == ')' and len(stack) != 0:
            stack.pop()
        elif st == ')' and len(stack) == 0:
            print("NO")
            flag = False
            break

    if not flag:
        continue

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
"""
# 카운팅
from sys import stdin

for _ in range(int(stdin.readline().strip())):
    sts = stdin.readline().strip()
    count = 0

    for st in sts:
        if st == '(':
            count += 1
        elif st == ')':
            count -= 1
        if count < 0:
            print("NO")
            break

    if count > 0:
        print("NO")
    elif count == 0:
        print("YES")