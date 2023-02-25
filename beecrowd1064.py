count=0
sum=0
for i in range(6):
    x=float(input())
    if x>0:
     count+=1
     sum=sum+x
     avr=sum/count
print(f"{count} valores positivos")
print(f"{avr:.1f}")
