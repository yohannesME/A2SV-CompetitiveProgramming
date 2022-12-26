class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #maximum index 
        maxIndex = 0
        
        #run through the nums and check if how long we can jump.
        for index, jump in enumerate(nums):
            if jump+index > maxIndex:
                maxIndex = jump + index
            elif index == maxIndex:
                break

        #check if the max Index is has reached or surpassed the final index    
        if maxIndex+1 >= len(nums):
            return True
        else:
            return False
            