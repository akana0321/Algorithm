"""
    럭키 스트레이트
     - 럭키 스트레이트 사용 조건 : 수를 반으로 나눠서 양쪽의 합이 같을 때
     - 입력 : N (10 <= N <= 99,999,999), 항상 짝수 형태로 주어짐
     - 출력 : 사용할 수 있다면 LUCKY, 사용할 수 없다면 READY
"""
from sys import stdin
n = list(map(int, stdin.readline().strip()))
half = int(len(n) / 2)
left = sum(n[:half])
right = sum(n[half:])

if left == right:
    print("LUCKY")
else:
    print("READY")