test_cases=int(input())
for i in range(test_cases):
    number=int(input())
    for j in range(1,number+1):
        print('*'*j,end='')
        print('#'*((number-j)*2),end='')
        print('*'*j,end='\n')
