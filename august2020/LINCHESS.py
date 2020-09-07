for T in range(int(input())):
    n, k=[int(x) for x in input().split()]
    p=[int(x) for x in input().split()]
    m=[]
    for i in p:
        if(k%i==0):
            m.append(i)
    if(len(m)<1):
        print(-1)
    else:
        print(max(m))
