# Write a Python program to create a flat list of all the values in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the values of the said flat dictionary:
# [19, 20, 21, 20]

old_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

# I iterate over the values of the dict and I append them to a previously created lict

values = []

for val in old_dict.values():
    values.append(val)

print(values)
