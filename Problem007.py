from math import floor, sqrt

def isPrime(x):
    if x in [ 2, 3, 5]:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(3, floor(sqrt(x)) +1, 2):
        if x % i == 0:
            return False
    return True


a = 0
prime_number = 10001
num=2
while( True):
    if isPrime(num):
        a+=1
        print(a, num)
        if a == prime_number:
            break
    num+=1

print("The prime number {} is {}".format(a, num))