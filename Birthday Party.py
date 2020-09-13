t=int(input())
for i in range(t):
    N,M=input().split()
    N=int(N)
    M=int(M)
    for i in range(1,M//N+2):
        if N*i==M:
            print("Yes")
            break
    else:
        print("No")