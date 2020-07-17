def sum_of_digits(n):
    sol=0
    while(n>0):
        sol+=n%10
        n//=10
    return sol

for T in range(int(input())):
    chef=0
    morty=0
    N=int(input())
    for i in range(N):
        x,y=[int(z) for z in input().split()]
        c=sum_of_digits(x)
        m=sum_of_digits(y)
        if(c==m):
            chef+=1
            morty+=1
        elif(c>m):
            chef+=1
        else:
            morty+=1
    if (chef==morty):
        print(2, chef)
    elif(chef>morty):
        print(0, chef)
    else:
        print(1, morty)
