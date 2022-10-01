class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, num = 0,0
        while num < len(nums) and zero < len(nums):
            if nums[zero] != 0:
                zero += 1
            if nums[num] == 0:
                num += 1
            elif nums[num] != 0 and num < zero:
                num += 1
                
            if num < len(nums) and zero < len(nums) and nums[num] != nums[zero] :
                nums[zero], nums[num] = nums[num], nums[zero]
                


        
            
                
        
        
