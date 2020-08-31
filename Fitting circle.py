n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        print(int(a/b))
    elif b>a:
        print(int(b/a))
    else:
        print("1")