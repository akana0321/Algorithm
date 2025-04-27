def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fg = fib_generator()
for _ in range(10):
    print(next(fg), end=" ")