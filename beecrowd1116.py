n=int(input())
for i in range (n):
    x,y=(map(int,input().split()))
    if y==0 and x>0 or x<0:
        print("divisao impossivel")
    else:
        z=x/y
        print("%.1f"%z)
    