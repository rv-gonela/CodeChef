from collections import Counter
from itertools import repeat
for T in range(int(input())):
    N=int(input())
    sol=0
    flag=True
    A=[int(x) for x in input().split()]
    B=[int(x) for x in input().split()]
    C=A+B
    C.sort()
    for i in range(0,2*N-1,2):
        if(C[i]!=C[i+1]):
            flag=False
            print(-1)
            break
    if(not flag):
        continue
    A=Counter(A)
    B=Counter(B)
    extraA=sorted((A-B).items())
    extraB=sorted((B-A).items())
    la=[]
    lb=[]
    for num,freq in extraA:
        la.extend(repeat(num,freq//2))
    for num,freq in extraB:
        lb.extend(repeat(num,freq//2))
    wildcard=2*C[0]
    n=len(la)
    for i in range(n):
        temp=min(la[i],lb[n-i-1])
        if(temp<wildcard):
            sol+=temp
        else:
            sol+=wildcard
    print(sol)
