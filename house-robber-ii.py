class Solution:
    def dp(self, nums, index, memo):
        N = len(nums)

        #the first choice is either first element or second, but then we can take the i+2, i+3 element because if we consider only i + 2 then we might miss out on the i+3 so just take the one which is better
        if index in memo:
            return memo[index]
            
        if index >= N:
            return 0
        
        #no need to memoize as it only is called once
        if index == -1:
            return max(self.dp(nums, 0, memo), self.dp(nums, 1,memo))

        
        memo[index] =  max(nums[index]+self.dp(nums, index+2, memo), nums[index]+self.dp(nums, index+3,memo))
        return memo[index]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.dp(nums[1:], -1, {}), self.dp(nums[:-1], -1, {}))