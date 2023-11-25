# Write a Python program to transform a dictionary into a list of tuples.
# Sample Output:
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]


my_dict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
my_list = []


for key, value in my_dict.items():
    my_list.append((key, value))

print(my_list)
