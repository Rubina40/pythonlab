#if name is less than 3 characters long - name must be at least 3 characters otherwise
#if uts more than 50 characters - name must be maximum of 50 character otherwise -name long
name = str(input("Enter your name:"))
length=len(name)
if length<3:
    print("Name must be atleast 3 characters long")
elif length>50:
    print("Name must be maximum of 50 characters")
else:
    print("Nice  name")