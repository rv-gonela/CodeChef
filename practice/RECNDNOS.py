T=int(input())
for i in range(T):
    n=int(input())
    l=[int(x) for x in input().split()]
    d={}
    d[l[0]]=1
    for j in range(1,len(l)):
        if(l[j]!=l[j-1]):
            if(l[j] not in d.keys()):
                d[l[j]]=1
            else:
                d[l[j]]=d[l[j]]+1
        else:
            l[j]=0
    m=max(d.values())
    sol=[]
    for i in d:
        if(d[i]==m):
            sol.append(i)
    print(min(sol))
