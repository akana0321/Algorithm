"""
    동전 0(https://www.acmicpc.net/problem/11047)
     - 입력 : N K (1 <= N <= 10, 1 <= K <= 100,000,000)
             이후 동전의 가치 Ai가 오름차순으로 주어짐(1 <= Ai <= 1,000,000, A1 = 1, i >=2 인 경우에 Ai는 ai-1의 배수)
     - 출력 : K원을 만드는데 필요한 동전 개수의 최솟값을 출력
"""
from sys import stdin

n, k = map(int, stdin.readline().split())
coins = [int(stdin.readline().strip()) for _ in range(n)]
coins.sort(reverse=True)
count = 0

for coin in coins:
    if k >= coin:
        count += k // coin
        k %= coin
    if k == 0:
        break

print(count)