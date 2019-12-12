"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

from string import ascii_uppercase

alpha_pos = {letter:i+1 for i, letter in enumerate(ascii_uppercase)}

def t_n(n):
    return (n+1)*n //2

def is_triangle(word):
    return sum(alpha_pos[letter] for letter in word) in lookpu_tn


with open("files/Problem042.txt", "r") as fin:
    input_data = fin.read().split(",")

lookpu_tn = {t_n(n) for n in range(1, 1000)}
input_data = [i.replace('"', "") for i in input_data]

result = [word for word in input_data if is_triangle(word)]

print(len(result))


