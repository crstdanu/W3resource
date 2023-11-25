# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# creez un dictionar gol
# iterez intr-un range de la 1 la 16 (ca sa am numerele de la 1 la 15)
# cheia va fi elementul iar valoarea va fi patratul elementului


my_dict = {}
for el in range(1, 16):
    my_dict[el] = el**2

print(my_dict)
