"""
    숨바꼭질(https://www.acmicpc.net/problem/1697)
     - 현재 수빈이는 점 N(0 <= N <= 100,000), 동생은 점 K(0 <= K <= 100,000)에 위치
        수빈이는 걷거나 순간이동 가능, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동 가능
        순간이동하는 경우 1초 후에 2*X의 위치로 이동
     - 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램 작성
     - 입력 : N K
     - 출력 : 동생을 찾는 가장 빠른 시간
"""
from sys import stdin
from collections import deque
INF = int(1e9)


def bfs(start, target):
    dist = [0] * INF
    dq = deque([start])

    while dq:
        now = dq.popleft()

        if now == target:
            return dist[now]

        for move in [now-1, now+1, now*2]:
            if 0 <= move <= INF and dist[move] != 0:
                dist[move] = dist[now] + 1
                dq.append(move)


n, k = map(int, stdin.readline().split())
print(bfs(n, k))



"""
 ####### 재귀함수로 풀기 #######
from sys import stdin


def solution(n, k):
    if n >= k:
        return n - k
    elif k == 1:
        return 1
    elif k % 2:
        return 1 + min(solution(n, k-1), solution(n, k+1))
    else:
        return min(k - n, 1 + solution(n, k//2))


n, k = map(int, stdin.readline().split())
print(solution(n, k))
"""