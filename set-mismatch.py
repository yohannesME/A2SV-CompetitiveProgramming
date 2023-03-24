class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lost = []
        N = len(nums)

        for i in range(N):
            while nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    lost.append(nums[i])
                    break
            
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        for i in range(N):
            #as we can find the value more than one remove duplicate by taking only one value
            lost = [lost[0]]
            if nums[i] != i+1:
                lost.append(i+1)
                return lost