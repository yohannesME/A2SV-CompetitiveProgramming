class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubArr = float('inf')
        _sum = 0
        N = len(nums)
        leftBound = 0
        rightBound = 0
        
        while rightBound < N:
            #traverse and update if the sum is greater of equal to target and leftBound move up
            if _sum >= target:
                minSubArr = min(minSubArr, rightBound-1 - leftBound + 1)
                _sum -= nums[leftBound]
                leftBound += 1
            #rightbound move if we have not reached target
            else:
                _sum += nums[rightBound]
                rightBound += 1 
        
        #as the upper while loop does not exhuast the final window we traverse through that
        while _sum >= target:
            minSubArr = min(minSubArr, rightBound-1 - leftBound + 1)
            _sum -= nums[leftBound]
            leftBound += 1            
        
        #check if min was never updated
        if minSubArr > N:
            return 0
        
        return minSubArr