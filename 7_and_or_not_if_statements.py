# conditional statements with logical operators

# AND OR NOT
#X is a separate condition
#Y is a separate condition

num = 20
city = "Shanghai"
country = "China"

#AND
#X and Y (This will return True only if both X and Y return True other False)

print(num >=20 and city == "Shanghai" and country == "China")
print(num > 20 and city == "Shanghai")
print(num == 20 and city == "Beijing")
print(num == 19 and city == "Beijing")

#OR
#X and Y (This is returns True only if one of X and Y return True other False)
print(num ==20 or city == "Beijing")
print(num >=20 or city == "Shanghai" or country == "China")
print(num == 19 or city == "Beijing")

#NOT
fruit = "apple"
print(fruit != "banana")
print(not(fruit == "banana"))

print(fruit != "apple")
print(not(fruit == "apple"))

#if statement
age = 20

if age >=25 and country == "China":
    print("Adult Chinese")

if age >=25 or country == "China":
    print("Chinese")

if age != 21:
    print("Hello World")

if not (age == 21) and not (country == "China"):
    print("Hello World Hello")

if not (age == 21) or not (country == "China"):
    print("Hello World Hello")

if age >= 18 and country == "China":
    print("Adult Chinese")
elif age >= 18 and country == "India":
    print("Adult Indian")
else:
    print("Marshian")

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print('Either of the number is greater than 0')
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")