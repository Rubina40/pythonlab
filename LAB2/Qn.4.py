#Given three integers, print the smallest one.(Three integers should be user input)

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1<num2 and num1<num3:
    print(f"The smallest number is {num1}")
elif num2<num1 and num2<num3:
    print(f"The smallest number is {num2} ")
else:
    print(f"The smallest number is {num3}")