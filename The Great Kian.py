n=int(input())
x=0
y=0
z=0
sum=0
sum1=0
sum2=0
numbers=list(map(int,input().split()))
for i in range(len(numbers)):
    x+=0+3*i
    y+=1+3*i
    z+=2+3*i
    if x<len(numbers):
        sum = sum + numbers[x]
    if y<len(numbers):
        sum1 = sum1 + numbers[y]
    if z<len(numbers):
        sum2=sum2+numbers[z]
    else:
        continue
    x=0
    y=0
    z=0
print(sum,end=' ')
print(sum1,end=' ')
print(sum2)

