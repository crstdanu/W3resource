# Write a Python program to convert a dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


original_dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
original_dict_2 = {'1': 'Austin Little', '2': 'Natasha Howard',
                   '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

# List comprehension
mylist1 = [[key, val] for key, val in original_dict_1.items()]
print(mylist1)

# Looping through the dictionary
mylist2 = []
for key, value in original_dict_2.items():
    mylist2.append([key, value])
print(mylist2)
