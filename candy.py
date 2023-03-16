class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        rightLeft = [1]
        leftRight = [1]
        output = 0
        
        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                rightLeft.append(rightLeft[-1]+1)
            else:
                rightLeft.append(1)
            
            if ratings[N-i] < ratings[N-i - 1]:
                leftRight.append(leftRight[-1] + 1)
            else:
                leftRight.append(1)

        for i in range(N):
            output += max(leftRight[i], rightLeft[N-1-i])

        return output