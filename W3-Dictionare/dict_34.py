# Write a Python program to count the number of items in a dictionary value that is a list.

my_dict = {
    "gaini": [5, 8, 65, 41, 25, 33, 71, 66, 2, 45],
    "porci": [3, 5, 2, 7, 6, 1, 9, 8],
    "cai": 5
}

# I will use the count() function on a dictionary value
# I will iterate through every dict item and if the item is a list I will print it's length


for k, v in my_dict.items():
    if isinstance(my_dict[k], list):
        print(f"Cheia '{k}' are o valoare de lungimea {len(v)}")
    else:
        print(f"Pentru cheia '{k}' valoarea nu este o lista")
