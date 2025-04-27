"""
    나무 자르기(https://www.acmicpc.net/problem/2805)
     - 절단기에 높이 H를 지정해야 함
     - 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라감, 이후 한 줄에 연속해 있는 나무 절단
     - 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않음
     - 여기서 잘라진 부분만 가져가는 것, 필요한 만큼만 딱 가져감
     - 입력 : 나무의 수 N(1 <= N <= 1,000,000) 가져가려는 나무의 길이 M(1 <= M <= 2,000,000,000)
             이후 각 나무의 높이들(1,000,000,000보다 작거나 같은 양의 정수)
                나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 집에 필요한 나무를 항상 가져갈 수 있다
     - 출력 : M미터의 나무를 가져가기 위한 절단기에 설정할 수 있는 높이의 최댓값
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    length = 0

    for tree in trees:
        if tree > mid:
            length += (tree - mid)

    if length >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
