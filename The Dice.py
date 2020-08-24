Dice_outputs=input()
x=0
if Dice_outputs[-1]=='6':
    print(-1)
else:
    for i in Dice_outputs:
        if i!='6':
            x += 1
        else:
            continue
    print(x)
