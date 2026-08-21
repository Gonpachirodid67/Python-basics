import random 

# generate a random  integer
print(random.randint(0, 10))

# generate a random integer between 0 and 1
print(random.random())

# selecting a random 'char' from a string
word = "Computer"
print(random.choice(word))

# generate a random float between 2 numbers
print(random.uniform(20, 50))

# generate a random integer in a range with step
print(random.randrange(0, 20, 3))

# random shuffle of items
fruits = ["apple", "orange", "guava", "watermelon"]
random.shuffle(fruits)
print(fruits)

# creates a random list from an existing one
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(random.sample(letters, k=2))