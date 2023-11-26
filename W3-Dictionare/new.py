def my_filtering_function(pair):
    key, value = pair
    if value >= 8.5:
        return True  # keep pair in the filtered dictionary
    else:
        return False  # filter pair out of the dictionary


grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}

filtered_grades = dict(filter(my_filtering_function, grades.items()))

print(filtered_grades)
