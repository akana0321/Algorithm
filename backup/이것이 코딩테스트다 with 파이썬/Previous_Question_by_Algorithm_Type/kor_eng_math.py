"""
    국영수
     - 1. 국어 점수가 감소하는 순서로
     - 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
     - 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
     - 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 옴)
     - 입력 : 반 학생 수 N(1 <= N <= 100,000)
             이후 한 줄에 하나씩 이름, 국어, 영어, 수학 점수가 공백으로(점수는 1이상 100이하)
             이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않음
     - 출력 : 위 조건대로 정렬하여 각 학생의 이름을 출력
"""
from sys import stdin

n = int(stdin.readline().strip())
students = [stdin.readline().split() for _ in range(n)]

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])