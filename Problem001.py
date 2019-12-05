import time

pair_of_numbers = [3, 5]
N = 1000  # This is the number that we have to find its divisibles


# There are some ways to do this, first we will look the iterative way

def is_divisible(number, pair):
    for i in pair:
        if number % i == 0:
            return True
    return False

    # More pythonic way to get this info although less readable
   # return all((number % i for i in pair)) # (Not Reachable)


start_time = time.time()
result = 0
for n in range(1, N):
    if is_divisible(n, pair_of_numbers):
        result += n
final_time = time.time()
print("The time spent {:.6f} to find the result {}".format(
    final_time - start_time, result))


# If we think a little bit harder we can make the program much scalable we can make this non iterative
def sum_of_numbers(i):
    return int(i*(i+1)/2)

start_time = time.time()
result = sum_of_numbers((N-1) // 3) * 3 + 5 * \
    sum_of_numbers((N-1) // 5) - 15 * sum_of_numbers((N-1)//15)
final_time = time.time()
print(f"The time spent with the fastest method {final_time - start_time:.6f} to find the result {result}")
