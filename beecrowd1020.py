d=int(input())
y=d//365
d=d%365
m=d//30
d=d%30
print(f"""{y} ano(s)
{m} mes(es)
{d} dia(s)""")
