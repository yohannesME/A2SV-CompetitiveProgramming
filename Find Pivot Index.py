class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if i != 0:
                left += nums[i-1]
            if right == left:
                return i
        return -1
        
        
