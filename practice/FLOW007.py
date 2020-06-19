t=int(input())
for i in range(t):
    sol=0
    x=int((input().strip()))
    while(x>0):
        sol=10*sol+x%10
        x=x//10
    print(sol)
