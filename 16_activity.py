# Activity 1

a = str(input("Enter a word: ").upper())

for i in a:
    if i == "A":
        print("A is found")
        break;
    else:
        print("A not found")

# Activity 2

for x in range(10):
        if x % 20 == 0:
            print("Twist")
        elif x % 15 == 0:
            print("Pass")
        elif x % 5 == 0:
            print("Fizz")
        elif x % 3 == 0:
            print("Buzz")
        else:
            print(x)

# Activity 3

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print("\nCurrent variable value: ", var)
print("\nGood Bye!")