a,b,c,d=(map(float,input().split()))
avg=(((a*2)+(b*3)+(c*4)+(d*1))/10)
print("Media: %.1f"%avg)
if avg>=7.0:
    print("Aluno aprovado.")
elif avg<5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    q=float(input())
    print("Nota do exame: %.1f"%q)
    av= ((avg+q)/2)
    if av>=5.0:
         print("Aluno aprovado.")
    else:
         print("Aluno reprovado.")
    print("Media final: %.1f"%av)

  

