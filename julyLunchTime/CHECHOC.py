for T in range(int(input())):
    n,m,x,y=[int(i) for i in input().split()]
    s=n*m
    if(s==1):
        sol=x
    elif(s%2==0):
        sol=(s//2)*min(2*x,y)
    else:
        sol=((s//2)*min(2*x,y))+min(x,y)
    print(sol)
