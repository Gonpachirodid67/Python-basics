# typecasting > change one type of data into another type
# example

age = 18

print(type(age)) # int

newAge = float(age)  # float

print(type(age)) # int

print(type(newAge)) # float

num1 = "25"
print(type(num1))

num2 = int(num1) # int
num3 = float(num1) # float

print(type(num2))
print(type(num3))

# city = "Jakarta"
# print(int(city))
# this will not work as letter cannot be converted into a integer

marks = 25
mymarks = str(marks) # string
print(type(mymarks)) # "25"
print(mymarks)