#If temperature is greater than 30, its hot day otherwise
#if its less than 10; its a cold day oyherwise neither cold nor hot.
temperature=(float(input("Enter today's temperature:")))
if temperature>30:
    print("It's a hot day")
elif temperature<10:
    print("It's a cold day")
else:
    print("Its neither hot nor cold day")