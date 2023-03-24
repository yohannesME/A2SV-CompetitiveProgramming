class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        duplicate = []
        N = len(nums)

        for i in range(N):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        for i in range(N):
            if nums[i] != i+1:
                duplicate.append(i+1)
                
        return duplicate