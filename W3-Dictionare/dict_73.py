# Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
# Sample Output:
# Original list of dictionaries:
# [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# Convert a list of dictionaries into a list of values corresponding to the specified key:
# [18, 22, 20, 18]

my_list = [
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]


list_of_values = []

for el in my_list:
    list_of_values.append(el["age"])

print(list_of_values)
