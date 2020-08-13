n=input().upper()
lst=['A','E','I','O','U','Y']
L=list(n)
if ((int(L[0])) + (int(L[1])))%2==0:
    if L[2] not in lst:
        if ((int(L[3])) + (int(L[4])))%2==0:
            if ((int(L[4])) + (int(L[5])))%2==0:
                if ((int(L[7])) + (int(L[8])))%2==0:
                    print("valid")
                else:
                    print("invalid")
            else:
                print("Invalid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")

