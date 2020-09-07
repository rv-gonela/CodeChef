def count(n):
    if(n<6):
        return n
    else:
        return n+count(n//2)

for T in range(int(input())):
    n=int(input())
    for i in range(n):
        trash=input()
    if(n<6):
      print(n)
    else:
      print(count(n))
