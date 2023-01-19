testcase = int(input())

#the answer
answer = []

for _ in range(testcase):

    #input size of the nubmer array
    n = int(input())

    #input the array
    nums = list(map(int,input().split()))

    nums.sort()

    for i in range(1,n):
        if abs(nums[i-1] - nums[i]) > 1:
            answer.append('NO')
            break
    else:
        answer.append('YES')


for ans in answer:
    print(ans)
