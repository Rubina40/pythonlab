# Write a python program to convert seconds to day,hour,minutes and seconds
second=int(input("Enter the time:"))
#into minutes
minute=second/60
hour=(second/60)/60
day=(((second/60)/60)/24)
remain_second=second*60
print(f"The current time is {day}days,{hour}hrs,{minute}mins and{remain_second}secs")