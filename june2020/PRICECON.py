T=int(input())
for i in range(T):
    k=int(input().split()[1])
    loss=0
    nums=[int(x) for x in input().split()]
    for y in nums:
        if (y>k):
            loss+=y-k
    print(loss)
