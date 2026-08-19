try:
    x = 10
    print(x)
except:
    print("An exception occured.")
finally:
    print("This is always run not matter what")


try:
    age = float(input("Enter your age: "))
    if age < 18:
        raise ValueError
    else:
        print("Welcome")
except ValueError:
    print("You are underage!")


try:
    # name error 
    y = 25
    print(y)
    age = float(input("Enter your age: "))
    if age < 18:
        raise ValueError
    else:
        print("Welcome")
except NameError:
    print("The variable does not exists")
except ValueError:
    print("Number less than 18 not allowed")
except:
    print("An exception occured")