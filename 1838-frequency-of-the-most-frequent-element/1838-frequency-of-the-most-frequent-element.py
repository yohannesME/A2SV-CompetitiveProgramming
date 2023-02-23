class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #sort the array
        nums.sort()
        N = len(nums)
        
        #our bounds and total as our prefix sum
        leftBound = 0
        rightBound = 0
        total = 0
        frequency = 0
        
        
        while rightBound < N:
            #add the total number value
            total += nums[rightBound]
            
            #if total + k is less than current value * the window size then we decrease the window
            while nums[rightBound]*(rightBound-leftBound+1) >total + k:
                total -= nums[leftBound]
                leftBound += 1
                
            #update frequency
            frequency = max(frequency, (rightBound-leftBound+1))
            rightBound += 1
        
        return frequency
        