# Write a Python program to remove a specified dictionary from a given list.

# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

original_list = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {
    'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

# I iterate over the elements os the list and if an element meets a criteria i remove it

# remove only the key:value pair that meets the criteria:
# del el['id']
# remove the entire list element:
# original_list.remove(el)

for el in original_list:
    if el['id'] == "#FF0000":
        # del el["id"]
        original_list.remove(el)

print(original_list)
