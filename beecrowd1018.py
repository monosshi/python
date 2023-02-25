m=int(input())
print(m)
 
for i in [100,50,20,10,5,2,1]:
  print(f"{m//i} nota(s) de R$ {i},00")
  m= m % i
  

  




