# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

lista_chei = ["x", "y", "z"]
lista_valori = [[el for el in range(11, 20)], [el for el in range(21, 30)], [
    el for el in range(31, 40)]]

my_dict = {key: val for (key, val) in zip(lista_chei, lista_valori)}


for key in my_dict:
    print(my_dict[key][4])
