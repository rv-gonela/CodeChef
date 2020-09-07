def power(b):
    r=1
    a2=2
    m=1000000007
    while(b>0):
        if(b & 1):
            r=(r*a2)%m
        b=b>>1
        a2=(a2*a2)%m
    return r

for T in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    for i in range(n):
        occ=power(n-i-1)
        print(occ,end=" ")
    print("")
    
