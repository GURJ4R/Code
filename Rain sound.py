import math
m=int(input())
for i in range(m):
    l,r,s=input().split()
    l=int(l)
    r=int(r)
    s=int(s)
    x=math.ceil(l/s)
    y=math.floor(r/s)
    if x>y:
        print(-1,-1)
    else:
        print(x,y)