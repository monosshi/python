

m=float(input())
if m>=0 and m<=1000000.00:
 print("NOTAS:")
for i in [100,50,20,10,5,2]:
  print(f"{int(m//i)} nota(s) de R$ {i}.00")
  m= m%i
print("MOEDAS:")
for i in [1,0.50,0.25,0.10,0.05,0.01]:
   print(f"{int(m//i)} moeda(s) de R$ {i:.2f}")
   m=m%i