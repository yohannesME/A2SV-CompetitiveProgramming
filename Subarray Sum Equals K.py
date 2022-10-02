class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumCount = 0
        subArray = 0
        prefix = {0:1}
        for num in nums:
            sumCount += num
            dif = sumCount - k
            
            subArray += prefix.get(dif, 0)
            prefix[sumCount]  = 1 + prefix.get(sumCount,0)
            
            
        return subArray
                
