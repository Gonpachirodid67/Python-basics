numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []

for num in numbers:
  if num % 2 == 0:
    even.append(num)

print(even)

odd = []

for num in numbers:
    if num % 2 == 1:
        odd.append(num)

print(odd)

# list comprehensions
evenNumbers = [num for num in numbers if num % 2 == 0]
oddNumbers = [num for num in numbers if num % 2 == 1]

print(evenNumbers)
print(oddNumbers)

# dictionary comprehensions
myDict = {str(num): num for num in numbers}

print(myDict)
print(type(myDict))
print(myDict['2'])

# map function
# map_object = map(function, iterable)
# myList = list(map_object)

def squared(n):
    return n**2

my_map = map(squared, numbers)
my_tuple = tuple(my_map)
print(my_tuple)

# lambda functions
my_cubes = list(map(lambda num: num**3, numbers))
print(my_cubes)


# filter
friends = ['Aakash', 'Avinash', 'Dinesh', 'Mukesh', 'Lokesh', 'Ajit']
invitations = list(filter(lambda friend: friend[0] == 'A', friends))
print(invitations)

roll_nos = [5, 7, 10, 1, 3, 2]

# zip(iterable1, iterable2)
combinedList = list(zip(friends, roll_nos))
print(combinedList)
print(type(combinedList[0]))

combinedTuple = tuple(zip(friends, roll_nos))
print(combinedTuple)

combinedDict = dict(zip(friends, roll_nos))
print(combinedDict)

# exit function

marks = [42, 50, 55, 75, 18, 36, 45]

for x in marks:
    if x < 33:
        print("Sombody failed in exam. So I am making a exit!!!!")
        exit()
    else:
        print(f"Passed the exam with {x} marks")


# Activtiy 1
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# using map
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Squares of numbers in list")
print(square)


# Activity 2
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}    
s3 = list(zip(s1, s2))
print(s3,"\n")

# Zip elements of two lists
# Print elements one by one, but elements of 2nd list will be in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

#   Zip into dictionary
stocks = ['Reliance', 'Infosys', 'TCS']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))


# Activity 3
for i in range(10):
    if i == 5:
        print(exit)
        exit()
    print(i)