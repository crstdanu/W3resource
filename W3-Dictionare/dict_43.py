# Write a Python program to convert more than one list to a nested dictionary.

# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]


serii = ['S001', 'S002', 'S003', 'S004']
nume = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
numere = [85, 98, 89, 92]

# folosesc dictionary comprehension si dau fiecarui item valoarea corespunzatoare

new_list = [{el:
             {key: value} for (key, value) in zip(nume, numere)}
            for el in serii]

print(new_list)
