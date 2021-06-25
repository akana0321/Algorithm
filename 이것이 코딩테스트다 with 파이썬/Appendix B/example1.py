'''
    M이상 N 이하의 소수를 모두 출력
     - 자연수 M과 N이 빈칸을 사이에 두고 주어진다 (1 <= M <= N <= 1,000,000)
     - 단, M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어짐
     - 한 줄에 하나씩, 증가하는 순서대로 출력
     
    -> 에라토스테네스의 채 알고리즘 활룡
'''

import math

m, n = map(int, input().split())
array = [True for i in range(1000001)] # 처음에 모든 수가 소수(True)인 것으로 초기화
array[1] = 0 # 1은 소수가 아님

for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
    if array[i] == True: # i가 소수인 경우
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# M부터 N까지의 모든 소수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)

