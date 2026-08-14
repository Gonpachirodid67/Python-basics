# Functions

# Basic Function
# function syntax
def greet():
    print("Hello")

greet() # calling or executing the function

# Functions with positional parameters - the arguments must follow the parameter order
# Functions with default argument
def greeting(name, greet_word="Hey"):
    print(f"{greet_word}, {name}")

greeting("Hello", "Shlok")
greeting("Hi", "Rohit")
greeting("Good morning", "Tarun") # have to be in the same format
greeting("Raj")

# Functions with keyword arguments
greeting(greet_word = "Good evening", name = "Peter")

# Function with return statement
def fullName(fname, lname):
    return f"{fname} {lname}"

fullName("Peter", "Parker") # Its ok even if the last name is in the first name's place

result = fullName("Parker", "Peter")
print(result)

def add_nouns(n1, n2):
    print("Hello World")
    return n1 + n2
#   print("Hello World")  # you can not put anything else after return

print(add_nouns(7,8))

# Lambda functions => anonymous functions
# Lambda arguments : expression

x = lambda a: a + 10
print(x(8))

def fav_food():
    return lambda food: f"My favourite food is {food}"

result = fav_food() # result = lambda food: f"My favourite food is {food}"
print(result("Pizza"))

# Function decorators

def changeCase(func):
    def myinner():
        return func().upper()
    return myinner 

@changeCase  # this is acts an wrapper, this will make the result in upper case
def myFunction():
    return "Hello World!"

print(myFunction())

# Recursive function - Function calling itself
# def printMyName(name):
#   print(f"{name}")
#   print("I am calling myself again")
#   printMyName("Shlok Barai")

# printMyName("Shlok Barai")

# Recurrsion - factorial 
# Finding the factorial of a number
# 5 => 5*4*3*2*1 => 120
# 10 => 10*9*8*7*6*5*4*3*2*1 => 3628800

def calcFactorial(n):
    if n == 0:
        return 1
    else:
        return n * calcFactorial(n - 1)

calcFactorial(10)
calcFactorial(5)
calcFactorial(0)

def my_function():
    """Demonstrates triple double qoutes
    docstrings and does nothing really."""

    return None

print(my_function())
print(my_function.__doc__)