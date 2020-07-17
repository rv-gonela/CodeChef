for T in range(int(input())):
    N=int(input())
    x=[]
    y=[]
    xfound=False
    yfound=False
    for i in range(4*N-1):
        (xtemp,ytemp)=input().split()
        x.append(xtemp)
        y.append(ytemp)
    x.sort()
    y.sort()
    for i in range(0,4*N-3,2):
        if( not xfound):
            if(x[i+1]!=x[i]):
                xfin=x[i]
                xfound=True
        if(not yfound):
            if(y[i+1]!=y[i]):
                yfin=y[i]
                yfound=True
        if(xfound and yfound):
            break
    if(not xfound):
        xfin=x[4*N-2]
    if(not yfound):
        yfin=y[4*N-2]
    print(xfin,yfin)
