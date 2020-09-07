import math

for T in range(int(input())):
    C, R= [int(x) for x in input().split()]
    cs=ceil(C/9)
    rs=ceil(R/9)
    if(cs<rs):
        print(0,cs)
    else:
        print(1,rs)
