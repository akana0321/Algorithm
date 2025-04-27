"""
    수리공 항승(https://www.acmicpc.net/problem/1449)
     - 입력 : 물이 새는 곳의 수 N, 테이프의 길이 L(N, L <= 1,000인 자연수)
             물이 새는 곳의 위치(<= 1,000)
     - 출력 : 보수에 필요한 테이프의 개수
"""
from sys import stdin

n, l = map(int, stdin.readline().split())
locations = list(map(int, stdin.readline().split()))
locations.sort()

count = 0
temp = 0

for location in locations:
    if temp < location:
        count += 1
        temp = location + l - 1

print(count)