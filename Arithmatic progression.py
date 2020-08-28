import math
n = int(input())
for i in range(n):
    A,B,C = map(int,input().split())
    if ((B-A)-(C-B)) == 0:
        print("0")
    else:
        print(math.ceil(abs((B-A-C+B))/2))
