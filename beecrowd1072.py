n=int(input())
count=0
for i in range (n):
    x=int(input())
    if x>=10 and x<=20:
        count+=1
        
        print(f"{count} in")
    else:
        print(f"{count} out")
    