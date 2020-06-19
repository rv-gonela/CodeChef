def computePleasure(str,spl):
    sum=0
    for x in range(len(str)):
        for y in range(x + 1, len(str) + 1):
            temp=str[x:y]
            if (temp in spl):
                sum=sum+spl[temp]
    return sum

T=int(input())
for i in  range(T):
    a=input().strip()
    b=input().strip()
    n=int(input())
    spl={}
    splCount={}
    #spl is a dictionary which maps liked strings to their beauty points
    for j in range(n):
        temp=input().split()
        spl[temp[0]]=int(temp[1])
    asp=[]
    bsp=[]
    for x in range(len(a)):
        for y in range(x + 1, len(a) + 1):
            temp=a[x:y]
            if(temp not in asp):
                asp.append(temp)
    for x in range(len(b)):
        for y in range(x + 1, len(b) + 1):
            temp=b[x:y]
            if(temp not in bsp):
                bsp.append(temp)
    asp.append('')
    bsp.append('')
    maxP=0
    for x in asp:
        for y in bsp:
            temp=computePleasure(x+y,spl)
            if(temp>maxP):
                maxP=temp
            else:
                continue
    print(maxP)
