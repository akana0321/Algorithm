
def convert_to_decimal(number, base):
    mulitplier, result = 1, 0
    while number > 0:
        result += number % 10 * mulitplier
        mulitplier *= base
        number = number // 10
    return result

def test_convert_to_demial():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("테스트 통과!")


test_convert_to_demial()
print(convert_to_decimal(111, 2))