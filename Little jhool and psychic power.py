n=input()
for i in range(len(n)-5):
    if (n[i]=='0' and n[i+1]=='0' and n[i+2]=='0' and n[i+3]=='0' and n[i+4]=='0' and n[i+5]=='0') or (n[i]=='1' and n[i+1]=='1' and n[i+2]=='1' and n[i+3]=='1' and n[i+4]=='1' and n[i+5]=='1'):
        print("Sorry, sorry!")
        break
else:
    print("Good luck!")