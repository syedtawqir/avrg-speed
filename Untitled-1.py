
#Three cyclists are riding at the speed of 10,20,30 km/h. find 
# the average and compare which cyclist is riding slower than the average speed?

cycle1=10
cycle2=12
cycle3=8
avrgspeed = (cycle1+cycle2+cycle3)/3
if cycle1 < avrgspeed :
    print("the cycle1 is slower than avrage")
elif cycle2 < avrgspeed :
    print("the cycle2 is slower than avrage")
elif cycle3 < avrgspeed :
    print("the cycle3 is slower than avrage")
else :
    print("invalid operation")
