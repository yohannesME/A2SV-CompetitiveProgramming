class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [nums[0]]
        
        for index in range(1, len(nums)):
            prefixSum.append(prefixSum[-1]+nums[index])
        
        return prefixSum