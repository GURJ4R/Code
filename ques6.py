t=int(input())
while t>0:
    n=int(input())
    k=2*n-2
    for i in range(0,n):
        for _ in range(0,k-(n-1)):
            print(end=" ")
        k-=1
        for j in range(i, i + 1):
            print("*"*(2*j+1), end="")
        print("")
    t-=1