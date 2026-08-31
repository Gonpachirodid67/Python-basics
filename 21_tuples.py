# tuple - ordered, indexed, allow duplicates, immutable

fruits = ("apple", "orange")

veggies = tuple(("potato", "tomato"))

colors = ("red",)

print(type(colors))

friends = ("paul", "jones", ["a", "b", "c"], "harry" )

friends_list = list(friends)

friends_list.pop()

friends_list.append("garry")

friends = tuple(friends_list)

print(friends)
friends[2][0] = "z"

print(friends)

# unpacking
countries = ("USA", "China", "Japan", "Indonesia", "Australia", "New Zealand")

(country1, country2,  country3, *others) = countries

print(country1)
print(country2)
print(country3)
print(others)
print(type(others))
