x,y=(map(float,input().split()))
i={1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
p=float(i[x])*y
print("Total: R$ %.2f"%p)