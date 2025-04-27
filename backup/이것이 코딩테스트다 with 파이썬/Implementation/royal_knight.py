'''
    왕실의 나이트
    8 X 8 좌표 평면
    이동방식
     - 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
     - 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
    좌표가 주어졌을 때 이동할 수 있는 경우의 수 출력
'''


''' 내 풀이
location = input()
rows = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8} # 문자를 숫자로 변환시기 위한 딕셔너리
points = [rows[location[0]], int(location[1])] # 문자를 숫자로 바꾸어 좌표로 전환
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)] # 모든 이동 방법 정의
count = 0

for step in steps:
    next_row = points[0] + step[0]
    next_col = points[1] + step[1]

    if 1 <= next_row <= 8 and 1 <= next_col <= 8: # 1 미만 8 초과면 칸을 벗어남
        print(next_row, next_col)
        count += 1


print(count)
'''

# 다른 사람 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1  # 아스키 코드로 바꿔서 바꾸는 듯?

# 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
