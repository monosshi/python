from re import S


s=int(input())
m=s//60
s=S%60
h=m//60
m=m%60
print(f"{h}:{m}:{s}")

