print("Calculator")

bruh = True

while(bruh):
    try:
        sui = (input("What is your question today (Power/Addition/Subtraction/Multiplication/Division/Area/Perimeter/Percent): ").lower())
        if sui == "square roots":
            print("Write the number of the square root and by what power you want to multiply it by.")
            print("Only enter numbers or it wont work")
            a = int(input("Enter the number here: "))
            b = int(input("Enter the power here: "))
            print("Power of the number: ", a**b)
            bruh = False
        elif sui == "addition":
            print("Enter the numbers whose sum you want to find out.")
            c = int(input("Enter number 1: "))
            d = int(input("Enter number 2: "))
            print("Sum of the numbers: ", c + d)
            bruh = False
        elif sui == "subtraction":
            print("Enter the numbers whose difference you want to know.")
            e = int(input("Enter number 1: "))
            f = int(input("Enter number 2: "))
            print("Difference of the numbers: ", e - f)
            bruh = False
        elif sui == "multiplication":
            print("Enter the numbers whose product you want to know.")
            g = int(input("Enter number 1: "))
            h = int(input("Enter number 2: "))
            print("Product of the numbers: ", g * h)
            bruh = False
        elif sui == "division":
            print("Enter the numbers whose quotient")
            i = int(input("Enter the numerator here: "))
            j = int(input("Enter the denominator here: "))
            print("Quotient of the numbers", i/j)
            bruh = False
        elif sui == "area":
            length = int(input("Enter length: "))
            width = int(input("Enter width: "))
            print("Area: ", length * width)
        elif sui == "perimeter":
            length = int(input("Enter length: "))
            width = int(input("Enter width: "))
            print("Perimeter: ", 2 * (length + width))
        elif sui == "percentage":
            number = float(input("Enter the number: "))
            percent = float(input("Enter the percentage: "))
            print("Answer: ", (number * percent) / 100)

        print("Only Yes or No question.")
        more = (input("Do you have more questions?(Yes/No) ").lower())
        if more == "yes":
            bruh = True
        elif more == "no":
            bruh = False

        else:
            raise Exception
    except Exception as e:
        print("Invalid input")