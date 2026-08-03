print("Calculator")

bruh = True

while(bruh):
    try:
        sui = (input("What is your question today (square roots/addition/subtraction/multiplication/division): ").lower())
        if sui == "square roots":
            print("Write the number of the square root and by what power you want to multiply it by.")
            print("Only enter numbers or it wont work")
            a = int(input("Enter the number here: "))
            b = int(input("Enter the power here: "))
            print(a**b)
            bruh = False
        elif sui == "addition":
            print("Enter the numbers whose sum you want to find out.")
            c = int(input("Enter number 1: "))
            d = int(input("Enter number 2: "))
            print(c + d)
            bruh = False
        elif sui == "subtraction":
            print("Enter the numbers whose difference you want to know.")
            e = int(input("Enter number 1: "))
            f = int(input("Enter number 2: "))
            print(e - f)
            bruh = False
        elif sui == "multiplication":
            print("Enter the numbers whose product you want to know.")
            g = int(input("Enter number 1: "))
            h = int(input("Enter number 2: "))
            print(g * h)
            bruh = False
        elif sui == "division":
            print("Enter the numbers whose quotient")
            i = int(input("Enter the numerator here: "))
            j = int(input("Enter the denominator here: "))
            print(i/j)
            bruh = False

        else:
            raise Exception
    except Exception as e:
        print("Invalid input")