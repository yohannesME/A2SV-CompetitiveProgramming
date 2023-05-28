class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i, target, memo={}):
            if (i, target) in memo:
                return memo[(i,target)]

            if i == len(nums):
                return 1 if target == 0 else 0
            
            memo[(i,target)] =  dp(i+1, target + nums[i]) + dp(i+1, target - nums[i])
            return memo[(i, target)]
        
        return dp(0, target)