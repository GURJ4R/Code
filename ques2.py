n,x,y=input().split()
n=int(n)
x=int(x)
y=int(y)
arr=list(map(int,input().split()))
c=0
for i in arr:
    if i>=x and i<=y:
        c+=1
    else:
        print("NO")
        break
if c==n:
    print("YES")