#N students take K apples and distributes them among each other evenly.the remaining (undivisible) part remainns in the
#basket.how many apples will each student get?how many apples will remain in the basket?the program reads the number
#N and k.it should print two answers for the questions above.

N = int(input("enter the number of studentd in class:"))
K = int(input("enter the number of apples:"))

apples_get = (K/N)

remaining_apples = (K%N)
print(f"Each student get {apples_get}")
print(f"The remaining apples are{remaining_apples}")