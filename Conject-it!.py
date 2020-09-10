T = int(input())
for i in range(T):
    N = int(input())
    while True:
        if N != 1:
            if N % 2 == 0:
                N = N / 2
            else:
                N = 3 * N + 1
        print("YES")
        break



