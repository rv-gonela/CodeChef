max=0
list=[]
for i0 in range(int(input())):
    list.append(int(input()))
list.sort()
l=len(list)
for i in range(l):
    temp=list[i]*(l-i)
    if(temp>max):
        max=temp
print(max)
