"""
    위에서 아래로
     - 입력되는 숫자들을 내림차순으로 정렬
"""
import sys
from sys import stdin

n = int(stdin.readline().strip())
data = [0 * n for _ in range(n)]
for i in range(n):
    data[i] = int(sys.stdin.readline().strip())
data.sort(reverse=True)
print(data)