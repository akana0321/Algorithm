"""
    반복수열(https://www.acmicpc.net/problem/2331)
"""
from sys import stdin
import math

num = [0]
idx = 1

a, p = stdin.readline().split()
p = int(p)
num.append(a)

while True:
    temp = 0
    flag = False
    for ele in num[idx]:
        temp += int(math.pow(int(ele), p))

    for i in range(1, len(num)):
        if num[i] == str(temp):
            print(i-1)
            flag = True
            break

    if flag:
        break
    else:
        num.append(str(temp))
        idx += 1


