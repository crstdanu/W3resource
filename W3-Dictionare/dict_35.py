# Write a Python program to sort Counter by value.

# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

sample_dict = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

expected_dict = dict(
    sorted(sample_dict.items(), key=lambda el: el[1], reverse=True))

print(expected_dict)
