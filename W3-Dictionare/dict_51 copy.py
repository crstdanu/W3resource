# A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

my_dict = {'Math': [88, 89, 90], 'Physics': [
    92, 94, 89], 'Chemistry': [90, 87, 93]}


def my_function(pair):
    k, v = pair
    new_v = []
    if k == "Math":
        for el in v:
            new_v.append(el + 1)
    elif k == "Physics":
        for el in v:
            new_v.append(el - 2)
    else:
        new_v = v
    return (k, new_v)


new_dict = dict(map(my_function, my_dict.items()))


print(new_dict)


# my_dictionary = dict(map(lambda (k, v): (k, f(v)), my_dictionary.items()))

# for key, val in my_dict.items():
#     if key == "Math":
#         for i in range(len(val)):
#             val[i] += 1
#     if key == 'Physics':
#         for i in range(len(val)):
#             val[i] -= 2

# print(new_dict)
