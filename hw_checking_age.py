age = int(input("Enter your age: "))

if isinstance(age, (int, float)) and not isinstance(age, bool):
    if age == 10 or age == 11 or age == 12 or age == 13 or age ==14 or age == 15 or age == 16 or age == 17 or age == 18 or age == 19 or age == 20:
        print("Your age is between 10 to 20 years old.")
    else:
        print("Your age is not between 10 to 20 years old.")
else:
    print("Please enter your age")