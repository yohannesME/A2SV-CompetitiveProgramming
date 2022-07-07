class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        maxs = []
        i = 0
        j = len(nums)
        while i < j:
            maxs.append(nums[i]+nums[j-1])
            i = i+1
            j = j-1
        return max(maxs)
        
