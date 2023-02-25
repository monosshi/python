s=float(input())
if s>=0 and s<=2000.00:
    print("Isento")
elif s>2000.01 and s<3000.00:
    t=s-2000.00
    p=t%10
    r=(t-p)*8/100
    u=p*18/100
print(r+u)
   
