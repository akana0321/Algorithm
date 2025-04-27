"""
    스위치 켜고 끄기(https://www.acmicpc.net/problem/1244)

"""
from sys import stdin


def reverse_switch(n):
    if switch_list[n] == 1:
        switch_list[n] = 0
    else:
        switch_list[n] = 1


def male(n):
    for i in range(n, switch_count+1, n):
        reverse_switch(i)


def female(n):
    reverse_switch(n)
    '''gap = min(switch_count - n, n)

    for i in range(1, gap+1):
        if switch_list[n-i] != switch_list[n+i]:
            break
        else:
            reverse_switch(n-i)
            reverse_switch(n+i)'''
    for k in range(switch_count//2):
        if n + k > switch_count or n - k < 1:
            break
        if switch_list[n+k] == switch_list[n-k]:
            reverse_switch(n+k)
            reverse_switch(n-k)
        else:
            break


switch_count = int(stdin.readline())
switch_list = [0]
switch_list.extend(list(map(int, stdin.readline().split())))
student_count = int(stdin.readline())
students = [list(map(int, stdin.readline().split())) for _ in range(student_count)]

for student in students:
    if student[0] == 1:
        male(student[1])
    else:
        female(student[1])

for i in range(1, switch_count, 20):
    print(*switch_list[i:i+20])
