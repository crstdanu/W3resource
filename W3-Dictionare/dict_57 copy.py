# Write a Python program to filter even numbers from a dictionary of values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}

# we create a function that returnes True/False for even or odd
def even_numbers(value):
    if value % 2 == 0:
        return True
    else:
        return False


first_dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [2, 3, 8]}
second_dict = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}


filtered_first = {key: list(filter(even_numbers, value))
                  for (key, value) in first_dict.items()}
filtered_second = {key: list(filter(even_numbers, value))
                   for (key, value) in second_dict.items()}

print(filtered_first)
print(filtered_second)
