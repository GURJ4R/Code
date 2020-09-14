t=int(input())
c=0
while t>0:
    s=input()
    for i in range(len(s)):
                if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                    c+=(len(s)-i)*(i+1)
    print(c)
    c=0
    t-=1