A=list(map(float,input().split()))
B=list(map(float,input().split()))
x1,y1=A
x2,y2=B
f=((x2-x1)**2 +(y2-y1)**2)**(1/2)
print("%.4f"%f)
