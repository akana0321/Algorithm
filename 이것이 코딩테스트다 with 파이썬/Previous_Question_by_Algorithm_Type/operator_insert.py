"""
    연산자 끼워넣기(https://www.acmicpc.net/problem/14888)
     - 입력 : 수의 개수 N(2 <= N <= 11)
             N개의 수(1 <= 수 <= 100)
             합이 N - 1인 4개의 정수가 주어지는데 각각 덧셈, 뺄셈, 곱셈, 나눗셈의 갯수
     - 출력 : 최댓값
             최솟값
"""
from sys import stdin

n = int(stdin.readline().strip())
num = list(map(int, stdin.readline().split()))
operators = list(map(int, stdin.readline().split()))

max_value = -1e9
min_value = 1e9

def dfs(i, now):
    global min_value, max_value
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대해 재귀적으로 수행
        if operators[0] > 0: # 더하기
            operators[0] -= 1
            dfs(i + 1, now + num[i])
            operators[0] += 1
        if operators[1] > 0: # 빼기
            operators[1] -= 1
            dfs(i + 1, now - num[i])
            operators[1] += 1
        if operators[2] > 0: # 곱하기
            operators[2] -= 1
            dfs(i + 1, now * num[i])
            operators[2] += 1
        if operators[3] > 0: # 나누기
            operators[3] -= 1
            dfs(i + 1, int(now / num[i]))
            operators[3] += 1

dfs(1, num[0])

print(max_value)
print(min_value)