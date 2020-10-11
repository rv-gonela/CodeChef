for T in range(int(input())):
    n=int(input())
    nums=[]
    count=0
    for i in range(n):
        nums.append([int(x) for x in input().split()])
    i=n
    while(i>1):
        if(i!=nums[0][i-1] and count%2==0):
            count+=1
        elif(i==nums[0][i-1] and count%2==1):
            count+=1
        i-=1
    print(count)
