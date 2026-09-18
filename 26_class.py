# Create a class
class student:
    grade = 10
    print("Hi I am a student of grade", grade)

# Create an object
ob = student()

# Activity 2

# Create a class
class Vehicle:

    # create init method
    def __init__(self, max_speed, mileage):

        # bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
modelX = Vehicle(240, 18)

# Access the variables inside init method
print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)


# Activity 3

# Create a class
class Parrot:

    # Class Attribute
    species = "bird"

    # Instance Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# Access the class attributes
print("Blu is a {}". format(blu.species))
print("Woo is also a {}".format(woo.species))

# Access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))