"""
    약수(https://www.acmicpc.net/problem/1037)
     - 양수 A가 N의 진짜 약수가 되려면 N이 A의 배수이고, A가 1과 N이 아니어야 함
       어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램
     - 입력 : N의 진짜 약수의 개수(50개 이하의 자연수)
             이후 N의 진짜 약수가 주어짐(2이상 1,000,000 이하의 자연수, 중복 X)
     - 출력 : N을 출력

     * 20210805 - 최소 공배수 구현만 하면 풀이 끝
     * 20210806 -> 모든 약수를 주니까 정렬을 하고 처음이랑 마지막 거만 곱하면 됨.....
"""
from sys import stdin
input = stdin.readline

count = int(input().strip())
nums = list(map(int, input().split()))
nums.sort()

print(nums[0] * nums[-1])
