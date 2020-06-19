for i0 in range(int(input())):
    s=input().strip()
    count=0
    i=0
    while(i<len(s)-1):
        if(s[i]!=s[i+1]):
            count+=1
            i+=1
        i+=1
    print(count)
