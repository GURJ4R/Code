n = int(input())
for i in range(n):
    N = int(input())
    x=bin(N)[2:]
    if all(j=='1' for j in x):
        print(int(x,2))
    else:
        print(int('1'*len(x[1:]),2))






