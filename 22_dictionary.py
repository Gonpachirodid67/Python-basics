# dictionary => ordered, unindexed, unique,

# create a dictionary
country = {
    "name": 'India',
    "population": '1.5B',
    "capital": 'New Delhi',
    "is_developing": True,
    "lanuguages": 144,
    "avg_temp": 30.5,
    "land_forms": ['Mountains', 'Beaches', 'Plateaus', 'Plains'],
}

# no of items in the dictionary
print(len(country))

# access a particular item
print(country["name"])
print(country["land_forms"])
print(country["capital"])
print(country.get("capital"))

# update any item
country["lanuguages"] = 201

# print the dictionary
print(country)

# add new items to the dictionary
country["official_language"] = "Hindi"

# print the dictionary
print(country)

# create dictionary using dictionary constructor
person = dict(name = 'Shlok', age = 15, place = 'Asia')
print(person)

# check the data type
print(type(person))
print(type(country))

# removing items from a dictonary
# pop(key)
country.pop("avg_temp")
print(country)

# popitem() - remove the last item
country.popitem()
print(country)

# clear() = clears a dictonary
# country.clear()
# print(country)

# del => deletes a dictionary
# del country
# print(country)

# loop over the keys of a dictionary
for key in country:
  print(key)

# loop over the values of a dictionary
for key in country:
  print(country[key])

# loop over the values
for value in country.values():
  print(value)

# loop over both keys and values
for key, values in country.items():
  print(key, ": ", values)

basket1 = {
    "fruits": 10,
    "veggies": 20
}

# wrong way = reference copying
# basket2 = basket1

# correct way = dict.copy()
# correct way = dict(basket1)
basket2 = basket1.copy()
print(basket2)
basket2["fruits"] = 15
print(basket2)
print(basket1)