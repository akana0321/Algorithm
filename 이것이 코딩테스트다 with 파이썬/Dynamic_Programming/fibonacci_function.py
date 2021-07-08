"""
    피보나치 함수
     1. 일반적인 피보나치 함수 코드(재귀적)
     2. 1 + 메모이제이션(Memoization : 한 번 구한 결과를 메모리 공간에 메모해두고
                                     같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법)
     3. 호출되는 함수 확인
     4. 반복적

    * 재귀 함수를 이용하여 다이나믹 프로그래밍 코드를 작성하는 방법은 큰 문제를 해결하기 위해 작은 문제를
      호출한다고 하여 탑다운(Top-Down:하향식, 메모이제이션) 이라고 말함
      - 메모이제이션은 탑다운 방식에 국한되어 사용하는 표현
      - 엄밀히 말하면 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념이므로 다이나믹 프로그램과는 별도의 개념
    * 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을 도출한다고 하여
      바텀업(Bottom-Up:상향식) 방식이라고 함
      - 바텀업 방식에서 사용되는 결과 저장용 리스트는 DP 테이블이라 부름
"""

def fibo_simple(x):
    if x == 1 or x == 2:
        return 1
    return fibo_simple(x - 1) + fibo_simple(x - 2)

print(fibo_simple(4))

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

def fibo_memoization(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo_memoization(x - 1) + fibo_memoization(x - 2)
    return d[x]

print(fibo_memoization(99))

# 호출되는 함수 확인
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]

pibo(6)
print()

# 피보나치 수열 소스코드(반복적 - 바텀업)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])