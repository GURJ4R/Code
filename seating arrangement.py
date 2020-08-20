test_cases=int(input())
for i in range(test_cases):
    seat_number= int(input())
    x = seat_number%12
    if x == 0:
        print(seat_number - 11, "WS")
    elif x == 1:
        print(seat_number + 11, "WS")
    elif x == 2:
        print(seat_number + 9, "MS")
    elif x == 3:
        print(seat_number + 7, "AS")
    elif x == 4:
        print(seat_number + 5, "AS")
    elif x == 5:
        print(seat_number + 3, "MS")
    elif x == 6:
        print(seat_number + 1, "WS")
    elif x == 7:
        print(seat_number - 1, "WS")
    elif x == 8:
        print(seat_number - 3, "MS")
    elif x == 9:
        print(seat_number - 5, "AS")
    elif x == 10:
        print(seat_number - 7, "AS")
    elif x == 11:
        print(seat_number - 9, "MS")