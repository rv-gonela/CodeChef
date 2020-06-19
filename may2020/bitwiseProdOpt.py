T=int(input())
for i in range(T):
    (x,y,l,r)=(int(x) for x in input().split())
    n=0
    z=0
    max=0
    while(l>(2**n)-1):
        n+=1
    while((2**n)-1<=r):
        z2=(2**n)-1
        max2=((x&z2)*(y&z2))
        if(max2>max):
            max=max2
            z=z2
            n+=1
        else:
            n+=1
            continue
    if(max==0):
        if((x&l)*(y&l)>=(x&r)*(y&r)):
            z=l
        else:
            z=r
    print(z)
