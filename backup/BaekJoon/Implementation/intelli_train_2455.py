"""
    지능형 기차(https://www.acmicpc.net/problem/2455)
     - 입력 : 각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 4줄
             기차의 정원은 10,000명
     - 출력 : 기차에 사람이 가장 많을 때의 사람 수
"""
from sys import stdin

out, ride = map(int, stdin.readline().split())
counts = [ride, 0, 0, 0]

for i in range(1, 4):
    out, ride = map(int, stdin.readline().split())
    counts[i] = counts[i - 1] - out
    counts[i] += ride

print(max(counts))