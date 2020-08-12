x,k = map(int, input().split())
str1=str(x)
str2=''
for digit in str1:
    if (digit!='9') and k>0:
        str2+='9'
        k-=1
    else:
        str2+=digit
print(int(str2))


