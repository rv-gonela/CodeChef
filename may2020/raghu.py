def op(l,i,j,k,o):
    temp=l[i]
    l[i]=l[k]
    l[k]=l[j]
    l[j]=temp
    o.append([i,j,k])
    return

def printAns(o):
    print(len(o))
    for a in o:
        print(a[0],a[1],a[2])

T=int(input())
for i1 in range(T):
    (n,kg)=(int(x) for x in input().split())
    l=[int(y) for y in input().split()]
    l.insert(0,0)
    mat=len(l)-1
    o=[]
    n=len(l)-1
    i=1
    succ=True
    flag=True
    while(True):
        if(len(o)>kg):
            succ=False
            break
        if(i==n+1):
            break
        if(l[i]==i):
            if(flag):
                mat=i
                flag=False
            i=i+1
            continue
        else:
            j=l[i]
            k=l[j]
            if(i==k):
                op(l,mat,j,k,o)
                #problem: l[j]=mat
                op(l,mat,j,l[j],o)
                i=i+1
                continue
            else:
                op(l,i,j,k,o)
                continue
    if(succ):
        printAns(o)
        #print(l)
    else:
        print(-1)
