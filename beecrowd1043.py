a,b,c=(map(float,input().split()))
per=float(a+b+c)
ar=float(0.5*(a+b)*c)
if (a+b)>c and (b+c)>a and (a+c)>b:
    print("Perimetro = %.1f"%per)
else:
    print("Area = %.1f"%ar)
