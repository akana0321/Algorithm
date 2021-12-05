"""
    킹(https://www.acmicpc.net/problem/1063)

"""
from sys import stdin
commands = {"R":[1, 0], "L":[-1, 0], "B":[0, -1], "T":[0, 1],
           "RT":[1, 1], "LT":[-1, 1], "RB":[1, -1], "LB":[-1, -1]}


def check_range(row, column):
    if ord('A') <= row <= ord('H') and 1 <= column <= 8:
        return True
    else:
        return False


def move(object, command):
    row = ord(object[0]) + command[0]
    column = int(object[1]) + command[1]
    if check_range(row, column):
        object = chr(row) + str(column)
        return object
    else:
        return False


def is_stone(king, stone):
    if king == stone:
        return True
    return False


# 앞에 잘라서 알파벳은 chr로 아스키 코드 변경하기
king, stone, count = stdin.readline().split()

for _ in range(int(count)):
    command = commands[stdin.readline().rstrip()]
    temp_king = move(king, command)
    temp_stone = move(stone, command)
    if not temp_king:
        continue
    else:
        if not is_stone(temp_king, stone):
            king = temp_king
        else:
            if temp_stone:
                king, stone = temp_king, temp_stone



print(king)
print(stone)
