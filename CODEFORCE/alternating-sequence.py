n = int(input())

#the answer
maximumSum = []

for _ in range(n):
    size = int(input())

    nums = list(map(int,input().split()))

    mSum = 0

    positive = 0
    negative = float('-inf')

    front = 0
    lookahead = 0
    while front < size and lookahead < size:
        if nums[front] > 0:
            positive = nums[front]
            #look ahead for more positive values consecutively
            lookahead = front + 1
            while lookahead < size:
                if nums[lookahead] > 0:
                    positive = max(positive, nums[lookahead])
                    lookahead += 1
                else:
                    break
            #add the largest positive number and update the front
            mSum += positive
            front = lookahead
        else:
            negative = nums[front]
            #look ahead for more negative numbers consecutively
            while lookahead < size:
                if nums[lookahead] < 0:
                    negative = max(negative, nums[lookahead])
                    lookahead += 1
                else:
                    break
            # add the largest negative number and update the front
            mSum += negative
            front = lookahead

    #add the answer to the array
    maximumSum.append(mSum)

for num in maximumSum:
    print(num)


