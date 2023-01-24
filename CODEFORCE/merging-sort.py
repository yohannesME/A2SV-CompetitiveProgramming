size1,size2 = list(map(int,input().split()))

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

output = []


arr2Pointer = 0

for num in arr1:

    if arr2Pointer < size2 and num <= arr2[arr2Pointer]:
        output.append(num)
    else:
        while arr2Pointer < size2 and arr2[arr2Pointer] < num:
            output.append(arr2[arr2Pointer])
            arr2Pointer += 1
        output.append(num)

if arr2Pointer < size2:
    output += arr2[arr2Pointer:]

for num in output:
    print(num,end=' ')
