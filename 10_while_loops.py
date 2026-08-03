num = 0

while (num < 10):
    print(num)
    num += 1

# this is how to make a string into float and not get stuck
# works for boolean, string, float and integer
condition = True
while(condition):
    try:
        user_input = float(input("Enter a number between 0 and 10: "))
        if user_input > 0 and user_input <= 10:
            condition = False
        else:
            raise Exception
    except Exception as e:
        print("Invalid input.")