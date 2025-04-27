"""
    정수 삼각형(https://www.acmicpc.net/problem/1932)
     - 입력 : 삼각형의 크기 n(1 <= n <= 500
             이후 정수 삼각형이 주어짐
     - 출력 : 합이 최대가 되는 경로에 있는 수의 합

     * 참고 : https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95
"""
from sys import stdin

n = int(stdin.readline().strip())
triangle = [[0] + list(map(int, stdin.readline().split())) + [0] for _ in range(n)]

for i in range(1, len(triangle)):
    for j in range(1, i + 2):
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))
