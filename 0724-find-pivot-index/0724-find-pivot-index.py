class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        
        #traverse through the array decrease the value and see if we find them to be equal
        for index in range(len(nums)):
            right -= nums[index]
            #the offset
            if index != 0:
                left += nums[index-1]
            #if equal then i is
            if right == left:
                return index
        #if we did not find anything return -1
        return -1
        
    
        