class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #inialize the variables
        sumCount = 0
        subArray = 0
        prefix = {0:1}
        
        #traverse the numbers
        for num in nums:
            #find the difference to that number and check in the prefix sum
            sumCount += num
            dif = sumCount - k
            
            subArray += prefix.get(dif, 0)
            prefix[sumCount]  = 1 + prefix.get(sumCount,0)
            
        #return all encounters
        return subArray
                