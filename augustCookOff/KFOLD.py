for T in range(int(input())):
    n,k=[int(x) for x in input().split()]
    s=input().strip()
    d={'0':0,'1':0}
    mul=n//k
    for i in s:
        d[i]+=1
    if(d['0']%mul!=0 or d['1']%mul!=0):
        print("IMPOSSIBLE")
        continue
    c0=d['0']//mul
    c1=d['1']//mul
    s0=('0'*c0)
    s1=('1'*c1)
    sol=""
    for i in range(mul):
        if(i%2==0):
            sol=sol+s0+s1
        else:
            sol=sol+s1+s0
    print(sol)
