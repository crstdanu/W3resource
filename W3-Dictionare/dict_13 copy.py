# Write a Python program to map two lists into a dictionary.


# map() is a function that applies a function to every element from within a list
# my function has to create key:value pairs from list items
# create the two lists

chei = ["vaci", "cai", "capre", "oi", "porci"]
valori = [12, 4, 25, 123, 75]

# I will use the zip() function to iterate over two lists and combine the elements with identical indexes into key:value pairs in my dictionary


my_dict = {key: value for (key, value) in zip(chei, valori)}

print(my_dict)

# sau

new_dict = {}

for key, value in zip(chei, valori):
    new_dict[key] = value

print(new_dict)
