"""
    바닥 공사
     - 가로 N, 세로 2의 직사각형 바닥 -> 1 x 2, 2 x 1, 2 x 2 세종류의 덮개를 이요해서 채우고자 함
     - 입력 : N
     - 출력 : 2 x N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지 출력
"""
from sys import stdin

n = int(stdin.readline().strip())
