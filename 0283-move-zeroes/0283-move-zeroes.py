class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #keep track of the index of a zero occurance
        zero = 0 
        #keep track of the non zero occurance
        num = 0
        
        while num < len(nums) and zero < len(nums):
            #check for a zero index
            if nums[zero] != 0:
                zero += 1
            #check for a non zero index
            if nums[num] == 0:
                num += 1
            #if the non zero is below or above the zero
            elif nums[num] != 0 and num < zero:
                num += 1
            
            #swap the zero and the non zero at the identified index
            if num < len(nums) and zero < len(nums) and nums[num] != nums[zero] :
                nums[zero], nums[num] = nums[num], nums[zero]
                


        
            
                
        
        