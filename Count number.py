import re
T=int(input())
for i in range(T):
    N=int(input())
    str=input()
    print(len(re.findall("\d+",str)))


