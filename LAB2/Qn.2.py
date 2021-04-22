#WAP which accepts marks of four subjects and display total marks,percentage and grade.
mark1=float(input("enter marks of subject 1:"))
mark2=float(input("Enter marks of subject 2:"))
mark3=float(input("enter marks of subject 3:"))
mark4=float(input("Enter marks of subject 4:"))
total_marks = mark1+mark2+mark3+mark4
percentage = (total_marks/400)*100
print(f"The total obtained marks is:{total_marks}")
print(f"The total percentage is:{percentage}%")
if percentage>=90:
    print("RESULT = Distinction")
    print("GRADE = A+")
elif percentage >= 80:
    print("RESULT = Distinction")
    print("GRADE = A")
elif percentage>=70:
    print("RESULT = 1st division")
    print("GRADE = B+")
elif percentage>=60:
    print("RESULT = 2nd Division")
    print("GRADE = B")
elif percentage>=50:
    print("RESULT = 3rd Division")
    print("GRADE = c+")
elif percentage>=40:
    print("RESULT = Just pass")
    print("GRADE = c")
else:
    print("RESULT = failed")
    Print("No grade")