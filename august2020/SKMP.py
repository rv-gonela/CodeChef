for T in range(int(input())):
    s=list(input().strip())
    p=input().strip()
    t=list(p)
    for i in t:
        s.remove(i)
    s.append(p)
    s.sort()
    if(p[0] in s):
        index=s.index(p)
        index2=s.index(p[0])
        s2=s.copy()
        s2.remove(p)
        s2.insert(index2, p)
        print(min("".join(s),"".join(s)))
    else:
        print("".join(s))
