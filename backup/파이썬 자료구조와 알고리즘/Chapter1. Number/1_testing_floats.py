from fractions import Fraction

def rounding_floats(number1, places):
    return round(number1, places)

def float_to_frations(number):
    return Fraction(*number.as_integer_ratio())

def get_denomiator(number1, number2):
    """ 분모를 반환 """
    a = Fraction(number1, number2)
    return a.denominator

def get_numerator(number1, number2):
    """ 분자를 반환 """
    a = Fraction(number1, number2)
    return a.numerator

def test_testing_floats():
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number6 = 6
    assert(rounding_floats(number1, number2) == 1.2)
    assert(rounding_floats(number1 * 10, number3) == 10)
    assert(float_to_frations(number1) == number4)
    assert(get_denomiator(number2, number6) == number6)
    assert(get_numerator(number2, number6) == number2)
    print("테스트 통과!")

test_testing_floats()

# assert란 무엇인가
t = 3.14
assert type(t) is int, '정수 아닌 값이 있네' # 정수가 아니면 AssertionError를 띄움