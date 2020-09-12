s=input()

prev=''

ans=0

l=[]

for i in s:
    if(i!=prev):
        ans+=1
    else:
        l.append(ans)
        ans=1
    prev=i

    l.append(ans)

print(max(l))