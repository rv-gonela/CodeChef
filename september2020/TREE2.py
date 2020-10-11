for T in range(int(input())):
    n=int(input())
    nums=set(input().split())
    if('0' in nums):
        nums.remove('0')
    print(len(nums))
