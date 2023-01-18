class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        #reverse and add at the end
        for i in range(len(nums)):
            nums.append(int(str(nums[i])[::-1]))

        #create a set and return the lenght
        return len(set(nums))