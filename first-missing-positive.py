class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        #cyclic sort the element but if only its positive and in the range of the size of the array and not already sorted
        for i in range(N):
            while nums[i] != i + 1 and 0 < nums[i] < N and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp

        #index + 1 that does not match the value is the answer or N + 1 is all are present
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1

        return N+1