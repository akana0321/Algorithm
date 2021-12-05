"""
    가장 긴 증가하는 수열(https://www.acmicpc.net/problem/12015)
     - 입력 : 수열 A의 크기 N(1 <= N <= 1,000,000)
             수열 A을 이루고 있는 Ai(1 <= Ai <= 1,000,000)
     - 출력 : 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력

     * 참고 : https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
from sys import stdin
import bisect

x = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
