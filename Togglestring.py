n=input()
str=''
for i in n:
    if i==i.lower():
        str=str+i.upper()
    elif i==i.upper():
        str=str+i.lower()
print(str)