# Write a Python program to invert a dictionary with unique hashable values.
# Sample Output:
# {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}


mydict = {
    "Theodore": 10,
    "Mathew": 11,
    "Roxanne": 9
}

newdict = {val: key for key, val in mydict.items()}

print(newdict)
