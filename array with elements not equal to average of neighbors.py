class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        output = []
        mid = int(len(nums)/2)
        i = mid
        j = mid

        while j >= 0 or i <= len(nums)-1:
            if(j>=0):
                output.append(nums[j])
            if(i != mid and i <= len(nums)-1):
                output.append(nums[i])

            i = i + 1
            j = j - 1
            
        return output
