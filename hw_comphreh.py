# 1. Odd numbers under the input value
num = int(input("Enter a number: "))

odd_numbers = [x for x in range(num) if x % 2 != 0]

print("Odd numbers:", odd_numbers)


# 2. Capitalize the first letter of every fruit
fruits = ["apple", "banana", "orange", "mango", "grape"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Capitalized fruits:", capitalized_fruits)