#Solution 1:
for T in range(int(input())):
    N=min(int(input()),64)
    count=1
    print('O', end="")
    for i in range(N-1):
        if(count%8==7):
            print('.')
        else:
            print('.', end="")
        count+=1
    for i in range(64-count):
        if(count%8==7):
            print('X')
        else:
            print('X', end="")
        count+=1



#Solution 2:
'''
for T in range(int(input())):
    N=int(input())
    count=1
    print('O', end="")
    if(N>=64):
        for i in range(63):
            if(count%8==7):
                print('.')
            else:
                print('.', end="")
            count+=1
        continue
    #end of case 1
    if(N%8==0):
        for i in range(N-1):
            if(count%8==7):
                print('.')
            else:
                print('.', end="")
            count+=1
        for j in range(8):
            if(count%8==7):
                print('X')
            else:
                print('X', end="")
            count+=1
        for j in range(64-count):
            if(count%8==7):
                print('.')
            else:
                print('.', end="")
            count+=1
        continue
    #end of case 2
    if(N<8):
        for i in range(N-1):
            print('.', end="")
            count+=1
        if(count%8==7):
            print('X')
        else:
            print('X', end="")
        count+=1
        for j in range(8-N-1):
            if(count%8==7):
                print('.')
            else:
                print('.', end="")
            count+=1
        for j in range(N+1):
            if(count%8==7):
                print('X')
            else:
                print('X', end="")
            count+=1
        for j in range(64-count):
            if(count%8==7):
                print('.')
            else:
                print('.', end="")
            count+=1
        continue
    #end of case 3
    for i in range(N-1):
        if(count%8==7):
            print('.')
        else:
            print('.', end="")
        count+=1
    for j in range(min(9, 64-N)):
        if(count%8==7):
            print('X')
        else:
            print('X', end="")
        count+=1
    for k in range(64-count):
        if(count%8==7):
            print('.')
        else:
            print('.', end="")
        count+=1
'''
