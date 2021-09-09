import math
import random

# 브루트 포스
def finding_prime(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

# 제곱근
def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True

# 확률론적 테스트와 페르마의 소정리
def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number - 1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number - 1, number) != 1:
                return False
        return True

num1 = 17
num2 = 20
print(finding_prime(num1))
print(finding_prime(num2))
print("-----------------------")
print(finding_prime_sqrt(num1))
print(finding_prime_sqrt(num2))
print("------------------------")
print(finding_prime_fermat(num1))
print(finding_prime_fermat(num2))