class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        N = len(nums)
        
        if N == 1:
            return nums[0]
        
        back = 0
        front = 1
        
        #check two elements at once
        while back < N and front < N:
            if nums[back] != nums[front]:
                return nums[back]
            
            back += 2
            front += 2
        
        #it must be that the last element is the non repeated one
        return nums[-1]