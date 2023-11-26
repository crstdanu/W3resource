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


def my_value(any_dict_list: list, any_key: str):
    my_result = []
    for el in any_dict_list:
        my_result.append(el[any_key])

    return my_result


lista_varsta = my_value(my_list, "age")
print(lista_varsta)
