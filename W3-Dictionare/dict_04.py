# Write a Python script to check whether a given key already exists in a dictionary.


my_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}


def check_for_key(cheie, dictionar: dict):
    if cheie in dictionar:
        print("Cheia este in dictionar")
    else:
        print("Cheia nu exista in dictionar")


check_for_key(8, my_dict)
