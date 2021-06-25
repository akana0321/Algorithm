'''
    1이 될 때까지
    어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
    단, 두 번째 연산은 N이 K로 나누어 떨어질 때만
    1. N에서 1을 뺀다
    2. N을 K로 나눈다
     - N(2 <= N <= 100,000), K(2 <= K <= 100,000)가 공백으로 구분, 자연수로
     - N은 항상 K보다 크거나 같음
     - N이 1이 될 때까지의 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값 출력
'''

n, k = map(int, input().split(' '))
result = 0

'''
while n >= k:
    다른 사람 풀이 -> n이 k로 나눠지지 않는다면 나눠질 때까지 1을 빼는 것 ㅣ < 부터
    while n % k != 0:                                            ㅣ
        n -= 1                                                   ㅣ
        result += 1                                              ㅣ < 까지    
    if n % k != 0:
        n -= 1
        result += 1
    else :
        n //= k
        result += 1
        
while n > 1:
    n -= 1
    result += 1
'''

# 제시된 수의 범위 초과일 경우 효율적인 코드
# N이 K의 배수가 되도록 한 번에 빼는 방식
while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1 씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복물 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)