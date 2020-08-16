str=input()
Z='z'
O='o'
count=1
sum=1
if str[0]!=Z or len(str)>20:
	print("No")
for i in str:
    if i==Z:
        count+=1
    elif i==O:
        sum+=1
    else:
        print("No")
if 2*(count-1)==(sum-1):
    print("Yes")
else:
    print("No")


