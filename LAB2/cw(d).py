#weight converter:
#input the weight of a person in either kg or lbs. if person provides his/her weight in kg
#convert it intp lbs else convert into kg
num=float(input("Enter your weight:"))
choose=input("kg or lbs:")
weight=float(num)
if choose=="kg":
    weight_1=weight*2.2406
    print(f"{weight}kg is equal to{weight_1}lbs")
else:
    weight_1=weight/2.2406
    print(f" {weight}lbs is equal to {weight_1}lbs")


