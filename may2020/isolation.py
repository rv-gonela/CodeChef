T=int(input())
for i in range(T):
    l2=input().split()
    n=int(l2[0])
    q=int(l2[1])
    dis=[0]*26
    ppl=input()
    for x in ppl:
        a=(ord(x)-ord('a'))
        dis[a]=dis[a]+1
    for y in range(q):
        qu=0
        c=int(input())
        for j in dis:
            if(j>c):
                qu=qu+j-c
        print(qu)
