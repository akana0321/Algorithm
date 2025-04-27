
name = "프레드"
print(f"그의 이름은 {name!r}입니다.")
print(f"그의 이름은 {repr(name)}입니다.") # repr ()은 !r과 같다

import decimal

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"결과: {value:{width}.{precision}}") # 중첩 필드 사용

from datetime import datetime

today = datetime(year=2021, month=8, day=18)
print(f"{today: %B %d, %Y}") # 날짜 포맷 지정자(specifier) 사용

number = 1024
print(f"{number:#0x}")