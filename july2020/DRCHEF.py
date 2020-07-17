for T in range(int(input())):
    (n,x)=[int(i0) for i0 in input().split()]
    l=[int(i0) for i0 in input().split()]
    l.sort()
    days=0
    inf=l.copy()
    m=l[n-1]
    i=0
    flag=True
    while(flag):
        while(i<n):
            temp=inf[i]
            if(temp<x/2):
                if(i==n-1):
                    flag=False
                i+=1
                continue
            elif(temp>=x/2 and temp<=x):
                x=2*temp
                inf[i]=0
                days+=1
                if(i==n-1):
                    flag=False
                break
            else:
                while(temp>x):
                    days+=1
                    inf[n-1]=min(2*(inf[n-1]-x),m)
                    x*=2
                break
    for i in range(n):
        if(inf[n-i-1]!=0):
            days+=1
    print(days)
