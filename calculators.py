print("Calculator")

bruh = True

while(bruh):
    try:
        calculator = (input("Which calculator do you want to use(Basic /Scientific /Graphing)?: ").lower())
        if calculator == "basic":
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