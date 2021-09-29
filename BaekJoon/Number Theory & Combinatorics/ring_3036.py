"""
    링(https://www.acmicpc.net/problem/3036)
     - 입력 : 링의 개수 N(3 <= N <= 100)
             링의 반지름(1과 1000을 포함하는 사이의 자연수)
     - 출력 : N-1줄 동안 첫 번째 링을 제외한 각각의 링에 대해서
            첫 번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력
"""
from sys import stdin


def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a


n = int(stdin.readline().strip())
rings = list(map(int, stdin.readline().split()))

denominators = [] # 분모
molecule = [] # 분자

for i in range(1, len(rings)):
    temp_gcd = gcd(rings[0], rings[i])
    denominators.append(rings[0]//temp_gcd)
    molecule.append(rings[i]//temp_gcd)

for i in range(len(denominators)):
    print("%d/%d" %(denominators[i], molecule[i]))
