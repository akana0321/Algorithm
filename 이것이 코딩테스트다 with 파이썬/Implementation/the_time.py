'''
    시각
     - 첫 줄에 정수 N이 입력된다 (0 <= N <= 24)
     - 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력
'''

n = int(input())
result = 0
start = [0, 0, 0]

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if i == 3 or j == 3 or k == 3:
                result += 1

print(result)