d=int(input())
c=0
for i in range(d):
    r,x=input().split()
    distance=(2*22/7*int(r))
    can_run=(100*int(x))
    if can_run>distance:
        c+=1
print(c)