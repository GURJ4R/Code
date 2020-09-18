D=int(input())
Oc,Of,Od=map(int,input().split())
Cs,Cb,Cm,Cd=map(int,input().split())
Sum_of_Cost_online_taxi=Oc+(D-Of)*Od
Sum_of_Cost_classic_taxi=Cb+(D/Cs)*Cm+D*Cd
if Sum_of_Cost_classic_taxi>Sum_of_Cost_online_taxi:
    print("Online Taxi")
else:
    print("Classic Taxi")