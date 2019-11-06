"""
Easy peasy

"""

N = 100
natural_sum = sum((i*i for i in range(1, N+1)))
sum_squared = sum((i for i in range(1, N + 1)))**2


print("Sum of squares ={} ".format(natural_sum))
print("Squared of the sum ={}".format(sum_squared))
print("The difference is = {}".format(sum_squared - natural_sum))
