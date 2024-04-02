while True:
    lastName = input("Enter student's last name or enter ZZZ to quit: ")
    if (lastName == "ZZZ"):
        break
    firstName = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if (gpa >= 3.5):
        print("Student made deans list")
    elif (gpa >= 3.25):
        print("Student made honor roll")