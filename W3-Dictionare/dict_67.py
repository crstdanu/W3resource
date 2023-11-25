# Write a Python program to invert a given dictionary with non-unique hashable values.
# Sample Output:
# {8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}

old_dict = {
    'Ora Mckinney': 8,
    'Mathew Gilbert': 8,
    'Theodore Hollandl': 7,
    'Mae Fleming': 7,
    'Ivan Little': 7
}

# I should transform every value into a key
# every corresponding key to that value has to go into a list of values (old keys)

# i iterate through the dicts' values and I add them as key to my new dict.
# if the key already exists in my new_dict I only append the new value to the list of values

new_dict = {}

for k, v in old_dict.items():
    if v not in new_dict.keys():
        new_dict[v] = [k]
    else:
        new_dict[v] += [k]

print(new_dict)
