class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #calculative Variable
        N = len(nums)
        #the average and the sum of the k elements
        maxAvg = float('-inf')
        subArrSum = 0
        #boundary to our sliding window
        leftBound = 0
        rightBound = k-1
        
        #create the slide window
        for i in range(k):
            subArrSum += nums[i]
    
        
        #move the window and calculate the average
        while leftBound < N and rightBound < N:
            maxAvg = max(maxAvg, subArrSum)
            subArrSum -= nums[leftBound]
            leftBound += 1
            rightBound += 1
            if rightBound >= N:
                break
            subArrSum += nums[rightBound]
            
            
        
        return maxAvg/k
        