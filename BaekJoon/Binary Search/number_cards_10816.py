"""
    숫자가드2(https://www.acmicpc.net/problem/10816)
     - N개의 숫자 카드 중에서 정수 M개가 주어졌을 때, 이 수가 적혀있는 카드가 몇개인지
     - 입력 : 카드의 개수 N(1 <= N <= 500,000)
             이후 N개의 정수, -10,000,000보다 크거나 같고 10,000,000보다 작거나 같다
             이후 찾을 수의 개수 M(1 <= M <= 500,000)
             이후 M개의 정수, -10,000,000보다 크거나 같고 10,000,000보다 작거나 같다
     - 출력 : M개의 수에 대해서, 각 수가 적힌 숫자 카드를 몇 개 갖고 있는지
                공백으로 구분해 출력

     * 참고 : https://hongcoding.tistory.com/12
"""
from sys import stdin

n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().split()))
nums.sort()
m = int(stdin.readline().strip())
targets = list(map(int, stdin.readline().split()))

hashMap = {}

for num in nums:
    if num in hashMap:
        hashMap[num] += 1
    else:
        hashMap[num] = 1

for target in targets:
    if target in hashMap:
        print(hashMap[target], end=' ')
    else:
        print(0, end=' ')

