

marks = int(input("Enter student's marks (1-100): "))

if marks < 1 or marks > 100:
    print("Invalid marks! Please enter between 1 and 100.")
else:
    if marks < 50:
        grade = "F"
    elif marks <= 60:
        grade = "E"
    elif marks <= 70:
        grade = "D"
    elif marks <= 80:
        grade = "C"
    elif marks <= 90:
        grade = "B"
    else:
        grade = "A"
    
    print("Grade:", grade)