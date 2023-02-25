count1=0
count2=0
count3=0
count4=0
for i in range(5):

   x=int(input())
   if x%2==0:
      count1+=1
   elif x%2!=0:
      count2+=1
   if x>0:
      count3+=1
   elif x<0:
      count4+=1
print(f'''{count1} valor(es) par(es)
{count2} valor(es) impar(es)
{count3} valor(es) positivo(s)
{count4} valor(es) negativo(s)''')
     
    

     
  