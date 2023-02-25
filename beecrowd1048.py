s=float(input())
per=int()
if   s>=0 and s<=400.00:
    per=15
elif s>400.00 and s<=800.00:
    per=12
elif s>800.00 and s<=1200.00:
    per=10
elif s>1200.00 and s<=2000.00:
    per=7
elif s>2000.00:
    per=4

earned=(s*per)/100
salary= s+earned

print(f'''Novo salario: {salary:.2f}
Reajuste ganho: {earned:.2f}
Em percentual: {per} %''')


