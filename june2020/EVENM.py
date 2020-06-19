# cook your dish here
for i0 in range(int(input())):
    n=int(input())
    i=1
    if(n%2==0):
        for x in range(0,n-1):
            for y in range(0,n):
                print(str(i),end=" ")
                i+=1
                if(y==n-1):
                    i+=1
            print("")
        x=n-1
        print(str(i),end=" ")
        i-=1
        for y in range(1,n):
            print(str(i),end=" ")
            i-=n+1
    else:
        for x in range(0,n):
            for y in range(0,n):
                print(str(i),end=" ")
                i+=1
            print("")
