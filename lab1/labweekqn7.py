# you live 4 miles away from university. the bus drives at 25mph but spends 2 minutes
# at each of the 10 stops on the way. how long will thebus journey take? alternatively,ypu could run
# to university . you jog the first time at 7mph,then run the next two at 15mph,before jogging the last at 7mph
# again ,will this be quicker or slower than the bus?
distance=4
speed=25
# bus stops at 10 stops for 2 minutes each
stop_t=10*2
time=distance/speed
hrs=time*60
total_time=hrs+stop_t
print(f"Total time to reach university by bus is:{total_time}")
#his runnig speed is7mph
speed1=7
time1=1/speed1
time_1=60*time1
speed2=15
time2=2/speed2
time_2=time2*60
speed3=7
time3=1/speed3
time_3=time3*60

total_time2=time_1+time_2+time_3
print(f"total time to reach by jogging is : {total_time2}")
if total_time2<total_time:
    print("Walking is faster to reach university")
else:
    print("Hence,going by bus will be faster")


