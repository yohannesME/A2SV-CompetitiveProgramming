class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        #the size of the number
        N = len(nums)
        #first lets take the equal adjacent values and change them
        for i in range(N-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
                i += 1
        
        #output
        output = [0]*N
        
        #map the non negative number to a new array
        index = 0
        for num in nums:
            if num != 0:
                output[index] = num
                index += 1
        
        
        return output