# Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

lista_originala = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [
    3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]


# I can iterate over every element in the list and make the first element the key and the other two the values
my_dict = {}
for el in lista_originala:
    my_dict[el[0]] = [el[1], el[2]]
print(my_dict)


# daca exista mai mult de 3 item-uri in fiecare element:
new_dict = {}
for elem in lista_originala:
    my_dict[elem[0]] = elem[1:]
print(my_dict)


# using dictionary comprehension
one_dict = {el[0]: el[1:] for el in lista_originala}
print(one_dict)
