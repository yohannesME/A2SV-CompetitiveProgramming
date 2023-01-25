class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #sort the array to adjust the pointers
        nums.sort()
        
        #right and left pointer
        leftBound = 0
        rightBound = len(nums)-1
        
        #number of operation
        operation = 0
        
        #while left does not cross the right
        while leftBound < rightBound:
            addedValue = nums[leftBound] + nums[rightBound]
            
            #if value found then operation increase and right and left move one step
            if addedValue == k:
                rightBound -= 1
                leftBound += 1
                operation += 1
            #if greater then right must move one step
            elif addedValue > k:
                rightBound -= 1
            #else left moves
            else:
                leftBound += 1
        
        return operation
        