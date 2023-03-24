class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #cyclic sort
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    return nums[i]

                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp