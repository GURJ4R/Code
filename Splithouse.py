n=int(input())
s=input()
if 'HH' in s:
    print("NO")
else:
    s=s.replace(".","B")
    print('YES')
    print(s)
