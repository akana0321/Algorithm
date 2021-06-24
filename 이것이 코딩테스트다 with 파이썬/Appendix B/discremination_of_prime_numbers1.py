'''
    이 방법은 2부터 x-1까지의 수를 나눠보면서 만약 떨어지는 수가 있다면,
    즉 해당 수의 약수가 된다면 소수가 아니므로 판별하는 방식
'''
# 소수 판별 함수
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x 가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


print(is_prime_number(4))
print(is_prime_number(7))