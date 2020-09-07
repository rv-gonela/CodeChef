for T in range(int(input())):
    hp, att=[int(x) for x in input().split()]
    if(hp>=2*att):
        print(0)
    else:
        print(1)
