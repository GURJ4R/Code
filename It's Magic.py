n = int(input())
val=list(map(int,input().split(" ")))
s=sum(val)
val1=[i for i in val if (s-i)%7==0]
if len(val1)!=0:
    print(val.index(min(val1)))
else:
    print(-1)
