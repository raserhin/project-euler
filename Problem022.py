"""
Using names.txt (https://projecteuler.net/project/resources/p022_names.txt) (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from time import time
from string import ascii_uppercase

with open("files/Problem022.txt", "r") as fin:
    input_data = fin.read().split(",")

input_data = [i.replace('"', "") for i in input_data]

start_time = time()
alpha_position = {letter:i+1 for i, letter in enumerate(ascii_uppercase)}
input_data.sort()
result = sum(sum(alpha_position[letter]  for letter in word) * (i+1)  for i, word in enumerate(input_data))
final_time = time()

print(result)