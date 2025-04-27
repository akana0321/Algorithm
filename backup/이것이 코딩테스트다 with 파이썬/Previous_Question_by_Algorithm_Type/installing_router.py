"""
    공유기 설치(https://www.acmicpc.net/problem/2110)
     - C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로
     - 입력 : 집의 개수 N(2 <= N <= 200,000), 공유기의 개수 C(2 <= C <= N)
             이후 집의 좌표 xn(1 <= xn <= 1,000,000,000)
     - 출력 : 가장 인접한 두 공유기 사이의 최대 거리
"""
from sys import stdin

n, c = map(int, stdin.readline().split())
array = [int(stdin.readline().strip()) for _ in range(n)]
array.sort()

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = array[0]
    count = 1
    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n): # 앞에서부터 순서대로 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)