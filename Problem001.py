import time 

pair_of_numbers=[3, 5]
N = 1000 # This is the number that we have to find its divisibles


# There are some ways to do this, first we will look the iterative way 

def is_divisible(number, pair):
    for i in pair:
        if number%i == 0:
            return True
    return False

start_time =time.time()
sum=0
for n in range(1, N):
    if is_divisible(n, pair_of_numbers):
        sum+=n
final_time=time.time()
print("The time spent {:.6f} to find the result {}".format(final_time - start_time, sum))


# If we think a little bit harder we can make the program much scalable we can make this non iterative
def sum_of_numbers(i):
    return int(i*(i+1)/2)
sum = sum_of_numbers((N-1) // 3) * 3 + 5 * sum_of_numbers((N-1) //5) - 15 * sum_of_numbers((N-1)//15)

print("The time spent with the fastest method {:.6f} to find the result {}".format(final_time - start_time, sum))