n=int(input())
for i in range (n):
    x,y,z=(map(float,input().split()))
    c = (x*2)+(y*3)+(z*5)
    d= c/10
    print("%.1f"%d)
    