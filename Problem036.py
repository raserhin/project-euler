from time import time


def is_pandigital(i):
    return str(i) == str(i)[::-1]


def is_both_pandigital(i):
    return is_pandigital(i) and is_pandigital(bin(i)[2:])


N = int(1e6)

start = time()
result = [i for i in range(1, N + 1) if is_both_pandigital(i)]

print("The result {} has been found in {:.6f}s".format(
    sum(result), time() - start))
