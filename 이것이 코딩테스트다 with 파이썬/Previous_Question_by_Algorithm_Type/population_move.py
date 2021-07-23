"""
    인구 이동(https://www.acmicpc.net/problem/18428)
     - 입력 : N, L, R(1 <= N <= 50, 1 <= L <= R <= 100)
             이후 N개의 줄에 각 나라의 인구수, r행 c열에 주어지는 정수는 A[r][c]의 값(0 <= A[r][c] <= 100)
             인구 이동이 발생하는 횟수가 2,000번보다 작거나 같은 입력만 주어짐
     - 출력 : 인구 이동이 몇 번 발생하는지
"""
from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = dx[::-1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # BFS를 위한 큐 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구수
    count = 1 # 현재 연합국가의 수
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라 확인
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

print(total_count)