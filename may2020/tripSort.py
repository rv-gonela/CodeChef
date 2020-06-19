def op(l,i1,i2,i3,o):
    temp=l[1]
    l[1]=l[3]
    l[3]=l[2]
    l[2]=temp
    o.append([i1,i2,i3])
    return

def printAns(o):
    print(len(o))
    for a in o:
        print(a[0],a[1],a[2])

T=int(input())
for i in range(T):
    (n,k)=(int(x) for x in input().split())
    l=[int(y) for y in input().split()]
    oper=[]
    for i1
    #insert code to implement algorithm here
    if(len(oper)>k):
        print(-1)
    else:
        printAns(oper)
