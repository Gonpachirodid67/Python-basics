# conditional statements
# we check for a condition => test => True or False
# if the test passes => True
# if the test fails => False

#if condition:
 # python statement

# if block will run only when the condiitions returns True
# if the condition fails and returns False then the code inside the if block will not run
# block

marks = -1

# nested conditional statement
if isinstance(marks, (int, float)) and not isinstance(marks, bool):
    if marks >=90 and marks < 100:
        print("You have cleared the exam and you have got A+")
    elif marks >=80 and marks < 90:
        print("You have cleared the exam and you have got A")
    elif marks >=60 and marks < 80:
        print("You have cleared the exam and you have got B+")
    elif marks >=40 and marks < 60:
        print("You have cleared the exam and you have got B")
    elif marks >=0 and marks < 40:
        print("You failed to clear the exam")
    else:
        print("Invalid marks. Please enter marks between 0 and 100")
else:
    print("The input is not a number")