'''
    이 방법은 2부터 x의 제곱근까지만 나눠보고 만약 나누어 떨어진다면,
    즉 해당 수의 약수가 된다면 소수가 아니므로 판별하는 방식
    예를 들어 16의 약수를 보면 1, 2, 4, 8, 16이 있는데 이는 가운데 약수를 기준으로
    대칭적으로 2개씩 앞뒤로 묶어서 곱하면 16을 만들 수 있다는 것을 확인할 수 있음.
    따라서 특정한 자연수 x가 소수인지 확인하기 위하여 바로 가운데 약수까지만
    나누어 떨어지는지 확인을 하면 된다.
'''

import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


print(is_prime_number(4))
print(is_prime_number(7))