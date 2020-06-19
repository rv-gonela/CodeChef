for i0 in range(int(input())):
    temp=int(input())
    wins=0
    count=0
    t=temp
    while(t%2==0):
        t//=2
        count+=1
    wins=temp//(2**(count+1))
    print(wins)
