from math import factorial

n = 20
m= 2* n  - 1

result = 2* factorial(m ) / factorial(m - n) / factorial(n) 
print( result)


