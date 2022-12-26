class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        #first assign missing 1+2+3+...+n
        missing = N*(N+1)/2
        
        #substract all the values in nums and we will find the missing one
        missing -= sum(nums)
        
        return int(missing)