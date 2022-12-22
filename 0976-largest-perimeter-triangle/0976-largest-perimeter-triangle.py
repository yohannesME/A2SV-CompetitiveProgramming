class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)-2):
            if sum(nums[-3-i:-1-i]) > nums[-1-i]:
                return sum(nums[-3-i:-1-i]) + nums[-1-i]
        return 0