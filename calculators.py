print("Calculator")
import math

bruh = True

while(bruh):
    try:
        calculator = (input("Which calculator do you want to use(Basic /Scientific /Graphing)?: ").lower())
        if calculator == "basic":
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Area")
            print("6. Perimeter")
            sui = int(input("Choose from 1 to 6: ").lower())
            if sui == "1":
                print("Enter the numbers whose sum you want to find out.")
                c = int(input("Enter number 1: "))
                d = int(input("Enter number 2: "))
                print("Sum of the numbers: ", c + d)
                bruh = False
            elif sui == "2":
                print("Enter the numbers whose difference you want to know.")
                e = int(input("Enter number 1: "))
                f = int(input("Enter number 2: "))
                print("Difference of the numbers: ", e - f)
                bruh = False
            elif sui == "3":
                print("Enter the numbers whose product you want to know.")
                g = int(input("Enter number 1: "))
                h = int(input("Enter number 2: "))
                print("Product of the numbers: ", g * h)
                bruh = False
            elif sui == "4":
                print("Enter the numbers whose quotient")
                i = int(input("Enter the numerator here: "))
                j = int(input("Enter the denominator here: "))
                print("Quotient of the numbers", i/j)
                bruh = False
            elif sui == "5":
                length = int(input("Enter length: "))
                width = int(input("Enter width: "))
                print("Area: ", length * width)
                bruh = False
            elif sui == "6":
                length = int(input("Enter length: "))
                width = int(input("Enter width: "))
                print("Perimeter: ", 2 * (length + width))
                bruh = False
            elif sui == "percentage":
                number = float(input("Enter the number: "))
                percent = float(input("Enter the percentage: "))
                print("Answer: ", (number * percent) / 100)
                bruh = False

            print("Only Yes or No question.")
            more = (input("Do you have more questions?(Yes/No) ").lower())
            if more == "yes":
                bruh = True
            elif more == "no":
                bruh = False
        if calculator == "scientific":
            print("1. Square")
            print("2. Power")
            print("3. Sine")
            print("4. Cosine")
            print("5.Tangent")
            options = int(input("Choose from 1 to 5: "))
            if options == "1":
                number = float(input("Enter number: "))
                print(number ** 2)
                bruh = False
            elif options == "2":
                num = int(input("Enter the number here: "))
                pow = int(input("Enter the power here: "))
                print("Answer: ", num**pow)
                bruh = False
            elif options == "3":
                angle = float(input("Enter angle: "))
                print(math.sin(math.radians(angle)))
            elif options == "4":
                