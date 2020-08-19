test_cases= int(input())
count=0
sum=0
for i in range(test_cases):
    green_price,purple_price = map(int,input().split())
    Total_student= int(input())
    for _ in range(Total_student):
        question1,question2 = map(int,input().split())
        if question1 == 1:
            count+= 1
        if question2 == 1:
            sum+= 1
    if green_price>purple_price:
        if count>sum:
            print(green_price*sum + purple_price*count)
        else:
            print(green_price*count + purple_price*sum)
    else:
        if count>sum:
            print(green_price*count + purple_price*sum)
        else:
            print(green_price*sum + purple_price*count)
    count=0
    sum=0