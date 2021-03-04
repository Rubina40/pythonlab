# A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class,print the smallest possible number of desk that can be purchased.
# The program should read three integers: the number of students in each classes,a,b and c respectively
# In the first test there are three groups. The  first group has 20 students and thus needs 10 desks.
# The second group has 21 students so they can get by with no fewer than 11 desks in total.

class1= int(input("Enter the number of students in class 1:"))
class2=int(input("Enter the number of students in class 2:"))
class3=int(input("Enter the number of students in class 3:"))

desk_class1 = (class1//2)
print(f"The required number of desk for class1 is: {desk_class1}")
desk_class2 = (class2//2)
print(f"The required number of desk for class2 is: {desk_class2}")
desk_class3 = (class3//2)
print(f"The required number of desk for class3 is: {desk_class3}")

remain_class1 = (class1%2)
print(f"Remainig desk for class 1 is: {remain_class1}")
remain_class2 = (class2%2)
print(f"Remainig desk for class 2 is: {remain_class2}")
remain_class3=(class3%2)
print(f"Remainig desk for class 3 is: {remain_class3}")
total_desk = desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 + remain_class3
print(f"Total number of desk that can be purchased is {total_desk}")