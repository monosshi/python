x=int(input())
y=int(input())
z=int(input())
if x>y and y>z:
    print(y,"is the 2nd largest num")
elif x<y and x>z:
    print(x,"is the 2nd largest num")
elif z<x and z>y:
    print(z,"is the 2nd largest num")
    
    
    