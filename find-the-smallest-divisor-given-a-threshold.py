class Solution:

    def withinThreshold(self, nums, threshold, mid):
        total = 0
        for num in nums:
            total += math.ceil(num/mid)
        
        return threshold >= total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = (left+right)//2

            if self.withinThreshold(nums, threshold, mid):
                right = mid
            else:
                left = mid + 1
        return right