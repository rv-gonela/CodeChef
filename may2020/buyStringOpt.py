T=int(input())
for i in  range(T):
    a=input().strip()
    b=input().strip()
    n=int(input())
    spl={}
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
    for x1 in asp:
        for y1 in bsp:
            sum=0
            str=x1+y1
            for x in range(len(str)):
                for y in range(x + 1, len(str) + 1):
                    temp=str[x:y]
                    if (temp in spl):
                        sum=sum+spl[temp]
            if(sum>maxP):
                maxP=sum
            else:
                continue
    print(maxP)
