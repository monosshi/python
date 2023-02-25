


from cmath import sqrt


a,b,c=(map(float,input().split()))
o=(b**2)-(4*a*c)
if o <0 or a==0:
    print("Impossivel calcular")

else:
    O=o**(1/2)
    r1=float()
    r2=float()

    r1= ((-b+O)/(2*a))
    r2= ((-b-O)/(2*a))
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)


