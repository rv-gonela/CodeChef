# cook your dish here
for T in range(int(input())):
    n,k,l=[int(x) for x in input().split()]
    if(n>k*l):
        print(-1)
        continue
    if(k==1 and n>1):
        print(-1)
        continue
    i=0
    j=1
    while(i<n):
        print(j,end=" ")
        j+=1
        if(j>k):
            j=1
        i+=1
    print("")