class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumHash = {}

        for i in range(len(nums)):
            if target - nums[i] in sumHash:
                return [i, sumHash[target-nums[i]]]
            
            sumHash[nums[i]] = i