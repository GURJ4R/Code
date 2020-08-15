N=int(input())
for i in range(N):
    N=N-i
    if N<0:
        print("Patlu")
        break
    N=N-i*2
    if N<0:
        print("Motu")
        break