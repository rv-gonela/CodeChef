for T in range(int(input())):
    n,k=[int(x) for x in input().split()]
    f=[int(x) for x in input().split()]
    tables=1
    l=[]
    for i in f:
        if(i in l):
            l=[]
            tables+=1
        l.append(i)
    print(tables)
