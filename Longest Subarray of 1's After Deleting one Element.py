class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lagging, fast = 0,0
        longest = 0
        deleted = 0
        while fast < len(nums):
            while fast < len(nums):
                if nums[fast] == 0:
                    deleted += 1
                if deleted > 1:
                    break
                fast += 1
                
            longest = max (longest, fast-lagging-1)
            
            while deleted > 1:
                if nums[lagging] == 0:
                    deleted -= 1
                lagging += 1
                
            fast += 1
            
        return longest        
