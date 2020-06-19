T=int(input())
for i in range(T):
    s=input().strip()
    r=list(s)
    temp=r[-1]
    r.pop(-1)
    r.insert(0,temp)
    l=list(s)
    temp=l[0]
    l.pop(0)
    l.append(temp)
    r=''.join(r)
    l=''.join(l)
    if(l==r):
        print('YES')
    else:
        print('NO')
