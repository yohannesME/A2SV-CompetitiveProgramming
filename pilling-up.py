# def checkCube(value, arr):
#     print(value, arr)
#     if len(arr) == 0:
#         print('Yes')
#         return
    
#     if arr[0]>arr[-1]:
#         if value >= arr[0]:
#             checkCube(arr[0], arr[1:])
#         else:
#             print('No')
#     else:
#         if value >= arr[-1]:
#             checkCube(arr[-1], arr[:-1])
#         else:
#             print('No')      
        
# T = int(input())
# for i in range(T):   
#     n = int(input())
#     blocks = [int(i) for i in input().split(' ')]
#     checkCube(float("inf"),blocks)
# this method uses recursion but because of the requirement of it being to much for the call stack it is not a suiteble place to use it.


T = int(input())
for i in range(T):   
    n = int(input())
    blocks = [int(i) for i in input().split(' ')]
    top = blocks[0] if blocks[0]>blocks[-1] else blocks[-1]
    l,r = 0, n-1
    while l < r:
        if blocks[l] >= blocks[r]:
            if top >= blocks[l]:
                top = blocks[l]
                l += 1
            else:
                print('No')
                break
        else:
            if top >= blocks[r]:
                top = blocks[r]
                r -= 1
            else:
                print('No')
                break
    if l == r:
        print('Yes')
        
      
