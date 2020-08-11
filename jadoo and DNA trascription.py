str = input().upper()
dict={'G':'C','C':'G','T':'A','A':'U'}
list = ['G', 'C', 'T', 'A']
for _ in str:
    if _ not in list:
        print("Invalid Input")
        exit()
for i in str:
    if i in dict:
        print(dict[i],end='')
    else:
        print("Invalid Input")
        break