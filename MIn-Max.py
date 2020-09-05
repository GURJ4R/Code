n=int(input())
array=list(map(int,input().split()))
for i in range(min(array),max(array)):
    if i not in array:
        print("NO")
        break
else:
    print("YES")