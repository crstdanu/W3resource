# A Python dictionary contains List as a value.
# Write a Python program to clear the list values in the said dictionary.
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

original_dict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

# I will iterate from each value and claer the element

for el in original_dict.values():
    el.clear()

print(original_dict)
