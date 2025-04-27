"""
    k번째 수(https://www.acmicpc.net/problem/1300)
     - NxN인 배열, A[i][j] = ixj
     - 이 수를 일차원 배열 B에 넣으면 B의 크기는 NxN이 됨
     - B를 오름차순 정렬했을 때, B[k]를 구해보자
     - A와 B의 인덱스는 1부터 시작
     - 입력 : 배열의 크기 N(<= 10^5인 자연수)
             이후 k, k의 크기는 min(10^9, N^2)보다 작거나 같은 자연수
     - 출력 : B[k]
"""
from sys import stdin

n = int(stdin.readline().strip())
k = int(stdin.readline().strip())
start, end = 1, k

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(1, n + 1):
        temp += min(mid//i, n)
    if temp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

