class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return bisect_left(nums,target)
        N = len(nums)
        left = 0
        right = N-1

        while left < right:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left + 1 if nums[left] < target else left