"""
    균형잡힌 세상(https://www.acmicpc.net/problem/4949)
     - 소괄호, 대괄호가 각각 쌍을 지어야 함
     - 각 문장의 끝은 .으로 끝남
     - 입력 : 하나 또는 여러줄에 걸쳐 문자열이 주어짐
                각 문자열은 영문 알파벳, 공백, 소괄호, 대괄호 등으로 구성
                길이는 100글자보다 작음
                입력의 종료조건으로 맨 마지막에 점 하나가 들어옴
     - 출력 : 각 줄마다 해당 문자열이 균형을 이루고 있으면 yes 아니면 no를 출력
"""
from sys import stdin

while True:
    sentence = stdin.readline().rstrip()
    stack = []

    if sentence == '.':
        break

    for character in sentence:
        if character not in "()[]":
            continue
        if character in "([":
            stack.append(character)
        elif character == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif character == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(0)
            break

    print("no" if stack else "yes")