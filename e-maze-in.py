str=input().upper()
list=[0,0]
for i in str:
    if i=="L":
        list[0]-=1
    if i=="R":
        list[0]+=1
    if i=="D":
        list[1]-=1
    if i=="U":
        list[1]+=1
print(list[0],end=" ")
print(list[1])
