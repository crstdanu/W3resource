# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
import random

# I create a variable to store my n number
# I loop through every number from 1 to n
# on every iteration i create a key and a value in my_dict
# my function returns the created dictionary


def generate(n: int):
    my_dict = {}
    for el in range(1, n+1):
        my_dict[el] = el * el
    return my_dict


n = 5

new_dict = generate(n)

print(new_dict)
