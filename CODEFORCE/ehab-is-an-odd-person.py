n = int(input())

nums = list(map(int,input().split()))

#even and odd count
evenCount = 0

for num in nums:
    if num%2 == 0:
        evenCount += 1

#if all numbers are even or odd print the inputed array
if evenCount == 0 or evenCount == n:
    print(*nums)
else:
    #sort the array
    nums.sort()

    #output the sorted elements
    print(*nums)
