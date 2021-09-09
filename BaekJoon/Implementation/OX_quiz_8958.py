"""
    OX 퀴즈
     - O는 1점 X는 0점
     - 입력 : 첫 줄에 테스트 케이스의 수
             이후 O와 X의 문자열, 길이는 0보다 크고 80보다 작음
     - 출력 : 각 테스트 케이스마다 점수를 출력
"""
from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    quiz = stdin.readline().strip()
    score = 0 # 더해가는 점수
    result = 0 # 결과
    for ele in quiz:
        if ele == 'X':
            score = 0
        else:
            score += 1
        result += score
    print(result)
