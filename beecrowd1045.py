list=[]
list=[float(x) for x in input().split()]
list.sort(reverse=True)

a=list[0]
b=list[1]
c=list[2]

if a>=(b+c):
    print("NAO FORMA TRIANGULO")
elif (a*a)==(b*b+c*c):
    print("TRIANGULO RETANGULO")
elif (a*a) > (b*b+c*c):
    print("TRIANGULO OBTUSANGULO")
elif (a*a) < (b*b+c*c):
    print("TRIANGULO ACUTANGULO")
if a==b and b==c:
    print("TRIANGULO EQUILATERO")
elif a==b or b==c or a==c:
    print("TRIANGULO ISOSCELES")

