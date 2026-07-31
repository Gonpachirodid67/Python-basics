# loops
# for loops - this file
# while loops
# nested loops

# for loops in strings
word = "watermelon ice cream"

# for loop syntax
for char in word: # u can use any word instead of char
    print("char")# - this will make it print every letter in a new line

# You can also add .lower() or .upper() behind char.lower()
# another way is:-
# for char in word:
#   if char == " ":
#     print("Hurray")
#   else:
#     print(char)

colors = ["Red", "Green", "Blue", "White", "Yellow", "Orange"]# python list

for color in colors:
    print(color)

# for range loops
# range(start, end, step)
# default start is 0 # where it will start from
# end is compulsory # where it will go till
# default step is 1 # step skips the amount of no. you enter 
print(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(3, 10, 2): # range will only work if the number is positive and nt negative
    print(i)

city = "Goa"
print(city[0])
print(city[1])

for i in range(len(word)):
    print(word[i])

for i in range(1, 11):
    print(f"5 X {i} = {i*5}")