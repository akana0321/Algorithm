"""
    요세푸스 문제 0(https://www.acmicpc.net/problem/11866)
     - 1번부터 N번까지 N명의 사람
     - 양의 정수 K(<=N)가 주어지는데, K번째 사람을 계속 제거하며 N명의 사람이 모두 제거될 때까지
     - 입력 : N K(1 <= K <= N <= 1,000)
     - 출력 : 요세푸스 순열 출력 ex) <3, 6, 2, 7, 5, 1, 4>

     * 참고 : https://yunaaaas.tistory.com/32
"""
from sys import stdin

n, k = map(int, stdin.readline().split())
q = [i for i in range(1, n+1)]
index = 0

print('<', end='')
while len(q) > 1:
    index += k
    if index > len(q):
        index %= len(q)
        if index == 0:
            index += len(q)
    index -= 1
    print(str(q.pop(index)), end=", ")

print(str(q.pop()) + '>')


