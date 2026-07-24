# nested conditional statements

# application admission process in a school
# criterion = nationality, marks

# nationality == filipino
# marks >= 50
# gender = 'male'

country = input("Enter your country name: ").lower()
marks = int(input("Enter your marks: "))
gender = input("Enter your gender (m/f): ")
nationality = "Not eligible"

if country == "philippines":
    nationality = "filipino"

if isinstance(marks, (int, float)):
    if nationality == "filipino":
        if gender == "m":
            if marks >= 50:
                print("Congratulations! You are selected for admission")
            else:
                print("Sorry, You are not eligible for admission")
        else:
            print("Sorry Only Boys are allowed for admission")
    else:
        print("Sorry, only filipinos are allowed for admissions")
else:
    print("Invalid marks!")

