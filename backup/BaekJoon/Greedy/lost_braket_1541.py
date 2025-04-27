"""
    잃어버린 괄호(https://www.acmicpc.net/problem/1541)
     - 양수와 +, - 괄호로 이루어진 식을 만들고 그 중에서 괄호를 지움
     - 적절히 괄호를 사용하여 최소값을 만들자
     - 입력 : 0~9, +, -로만 이루어져 있고, 가장 처음과 마지막 문자는 숫자
             연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다
             수는 0으로 시작할 수 있다.
             입력으로 주어지는 식의 길이는 50보다 작거나 같다
     - 출력 : 최솟값
"""
from sys import stdin

expression = stdin.readline().split('-')
result = 0

for i in expression[0].split('+'):
    result += int(i)

for i in expression[1:]:
    for j in i.split('+'):
         result -= int(j)

print(result)