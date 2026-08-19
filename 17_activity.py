try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 /  num2
    print("Result is: ", result)
# using multiple except block for different type of error

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like 1, 2")

except:
    print("Wrong Input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")