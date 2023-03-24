class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate = set()
        N = len(nums)

        for i in range(N):
            while nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    duplicate.add(nums[i])
                    break

                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        

        return list(duplicate)