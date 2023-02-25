# MONOSSHI ZAMAN
# ID-0182210012101147

time=input("What time is it?\n")
hour,min=[float(i)for i in time.split(":")]
dtime = hour+ (min/60)
def next_time(a):
    hour1=int(a)
    min1=int((a-int(a))*60)
    return(f"{hour1}:{min1}")
if dtime>24 or dtime<0:
    print("Invalid time")
elif 0<dtime<7:
    a=7-dtime
    print(f"Breakfast in {next_time(a)} hours")

elif 8>=dtime>=7:
    print("Breakfast time")
elif 8<dtime<12:
    a=12-dtime
    print(f"Lunch in {next_time(a)} hours")
elif 8<dtime>=12:
    print("Lunch time")
elif 13<dtime<18:
    a=18-dtime
    print(f"Dinner in {next_time(a)} hours")
elif 19>=dtime>=18:
    print("Dinner time")
elif 19<dtime<=24:
    a= (24-dtime)+7
    print(f"Breakfast in {next_time(a)} hours")
    





    
    

