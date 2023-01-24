size1,size2 = list(map(int,input().split()))

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

output = []

#track the smallest element to the current element in the first array
smallIndex = -1
for num in arr2:
    #find the smallest element and iterate until then
    while smallIndex+1 < size1:
        if arr1[smallIndex+1] < num:
            smallIndex += 1
        else:
            break

    #if nothing found add 0 else add 1 indexed value
    if smallIndex == -1:
        output.append(0)
    else:
        output.append(smallIndex+1)

for num in output:
    print(num,end=' ')
