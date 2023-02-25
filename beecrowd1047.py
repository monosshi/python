a,b,c,d=map(int,input().split())
s=a*60+b
e=c*60+d
dur=e-s
if dur<=0:
    dur=dur+24*60
hour=dur//60
min=dur%60
print(f"O JOGO DUROU {hour} HORA(S) E {min} MINUTO(S)")
