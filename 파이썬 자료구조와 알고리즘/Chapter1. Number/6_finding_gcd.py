# 유클리드 호제법
def finding_gcd(a, b):
    while(b != 0):
        result = b
        a, b = b, a % b
    return result

def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print("테스트 통과!")

print(finding_gcd(21, 12))
print(finding_gcd(25, 10))
test_finding_gcd()