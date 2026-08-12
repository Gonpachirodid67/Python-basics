# Functions

# Basic Function
def greet():
    print("Hello")

greet()

# Functions with positional parameters
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