"""
    계단 오르기(https://www.acmicpc.net/problem/2579)
     - 입력 : 계단의 개수
             제일 아래 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수
                계단의 개수는 300 이하, 점수는 10,000 이하의 자연수
     - 출력 : 얻을 수 있는 총 점수의 최댓값

    * 참고 : https://daimhada.tistory.com/181
"""
from sys import stdin

n = int(stdin.readline().strip())
stairs = [int(stdin.readline().strip()) for _ in range(n)]
dp = []

if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
else:
    dp.append(stairs[0])
    dp.append(max(stairs[0] + stairs[1], stairs[1]))
    dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

    for i in range(3, n):
        dp.append(max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i] + stairs[i - 1]))

    print(dp.pop())

