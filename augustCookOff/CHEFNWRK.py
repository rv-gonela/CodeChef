for T in range(int(input())):
    n,k=[int(x) for x in input().split()]
    nums=[int(x) for x in input().split()]
    trip=1
    total=0
    flag=True
    for i in nums:
        if(i>k):
            flag=False
            break
        temp=i+total
        if(temp>k):
            trip+=1
            total=i
        else:
            total=temp
    if(flag):
        print(trip)
    else:
        print(-1)
