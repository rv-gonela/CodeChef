T=int(input())
for i in range(T):
    (x,y,l,r)=(int(x) for x in input().split())
    max=None
    z=None
    temp=None
    for j in range(l,r+1):
        if(max is None):
            z=j
            max=(x&j)*(y&j)
        else:
            temp=(x&j)*(y&j)
            if(temp>max):
                z=j
                max=temp
    print(z)
