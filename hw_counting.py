condition = True
while(condition):
    try:
        number = float(input("Enter a number: "))
        if number > -99999999999999999999999999999999999999999999999999999999999999 and number <= 999999999999999999999999999999999999999999999999999999999999999999:
            counting = len(str(abs(number)))
            print("The toal number of digits in your input:", counting - 2)
            condition = False
        else:
            raise Exception
    except Exception as e:
        print("Invalid input.")