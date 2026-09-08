test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

frequency = {}

for value in test_dict.values():
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

print(frequency)