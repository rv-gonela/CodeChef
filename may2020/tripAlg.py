def op(l,i1,i2,i3,o):
    temp=l[i1]
    l[i1]=l[i3]
    l[i3]=l[i2]
    l[i2]=temp
    o.append([i1,i2,i3])
    return
l=[0,4,5,3,1,2]
o=[]

i=1
flag=True
while(True):
    if(i=n+1):
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
            i=i+1
            continue
        else:
            op(l,i,j,k,o)
            continue
print(l)
