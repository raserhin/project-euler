import time

N= int(4e6)

def fibonacci(n):
    """
        Generator of fibonacci sequence
    """
    a, b = 1, 2
    yield a
    yield b
    while b < n:
        a, b = b, a+b
        yield b

start_time=time.time()
result = sum((i for i in fibonacci(N) if i%2==0))
final_time=time.time()
print("Result {} found in just {:.6f}s".format(result, final_time-start_time))