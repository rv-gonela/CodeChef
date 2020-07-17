for T in range(int(input())):
    N=int(input())
    skipped=0
    list=[int(x) for x in input().split()]
    temp=list[0]
    for i in list[1:]:
        if(i!=temp):
            skipped+=abs(i-temp)-1
        temp=i
    print(skipped)
