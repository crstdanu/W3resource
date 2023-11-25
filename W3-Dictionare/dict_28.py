# Write a Python program to sort a list alphabetically in a dictionary.

# create a dictionary with a list of letters as a value

my_dict = dict(first=['o', 'g', 'w', 'c', "a", 'i', 'v'],
               second=["z", "q", "f", "m", "p", "b"])

# I run the dict through a loop to sort value by value

for k, v in my_dict.items():
    my_dict[k] = sorted(v)

print(my_dict)
