for T in range(int(input())):
    s=''
    n,step=[int(x) for x in input().split()]
    l=input().split()
    for i in l:
        dis=int(i)
        if(dis%step==0):
            s+='1'
        else:
            s+='0'
    print(s)
