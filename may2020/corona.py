T=int(input())
for i in range(T):
    n=int(input())
    ppl=[1]
    dis=[int(x) for x in input().split()]
    k=0
    for j in range(n-1):
        if((abs(dis[j]-dis[j+1]))>2):
            ppl.append(1)
            k=k+1
        else:
            ppl[k]=ppl[k]+1
    print(min(ppl),max(ppl))
