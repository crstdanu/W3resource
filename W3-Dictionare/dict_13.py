# Write a Python program to map two lists into a dictionary.


# map() is a function that applies a function to every element from within a list
# my function has to create key:value pairs from list items
# create the two lists

chei = ["vaci", "cai", "capre", "oi", "porci"]
valori = [12, 4, 25, 123, 75]


# create a function that takes the elements of two lists and joins them into a tuple

def lists_to_dict(elem1, elem2):
    return (elem1, elem2)


# the map function creates an object which is then transformed into a dict
my_dict = dict(map(lists_to_dict, chei, valori))

print(my_dict)
