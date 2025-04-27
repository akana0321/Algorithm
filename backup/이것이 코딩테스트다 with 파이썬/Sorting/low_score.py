"""
    성적이 낮은 순서로 학생 출력하기
     - 입력 : 첫 줄에는 학생 수(1 <= N <= 100,000), 다음에는 학생이름 성적 으로 입력
     - 출력 : 성적이 낮은 순으로 이름 출력

     * 16번 줄의 lambda 쓰는 법 알아두기
"""
from sys import stdin

n = int(stdin.readline().strip())
student = []
for _ in range(n):
    name, score = stdin.readline().split()
    student.append((name, int(score)))

student = sorted(student, key=lambda student: student[1])

for name in student:
    print(name[0], end=' ')