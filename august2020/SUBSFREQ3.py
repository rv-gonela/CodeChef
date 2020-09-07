from collections import Counter
def power(b,m):
    temp=1
    for i in range(b):
        temp=(temp*2)%m
    return temp

for T in range(int(input())):
    n=int(input())
    c=Counter([int(x) for x in input().split()])
    m=1000000007
    l=list(c.keys())
    l.sort()
    ls=len(l)
    j=0
    for i in range(1,n+1):
        if(j<ls and i==l[j]):
            occ=(power(n-i,m)*c[i])%m
            print(occ,end=" ")
            j+=1
        else:
            print(0,end=" ")
    print("")
