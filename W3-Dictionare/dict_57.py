# Write a Python program to filter even numbers from a dictionary of values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}


# I use dictionary comprehension

original_dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
filtered_dict = {key: list(el for el in value if (el % 2 == 0))
                 for (key, value) in original_dict.items()}
print(filtered_dict)

new_dict = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
very_new_dict = {key: list(el for el in value if (el % 2 == 0))
                 for (key, value) in new_dict.items()}

print(very_new_dict)
