def op(l,i,j,k,o):
    temp=l[i]
    l[i]=l[k]
    l[k]=l[j]
    l[j]=temp
    o.append([i,j,k])
    return l

def printAns(o):
    print(len(o))
    for a in o:
        print(a[0],a[1],a[2])


l=[0,3,2,4,1]
mat=len(l)-1
o=[]
n=len(l)-1
i=1
flag=True
while(True):
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
            continue
        else:
            l=op(l,i,j,k,o)
            continue
#print(l[1:])
printAns(o)
