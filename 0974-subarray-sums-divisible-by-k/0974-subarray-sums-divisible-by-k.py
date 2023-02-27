class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        subArr = 0
        sumVal = 0
        prefixSum = {0:1}
        
        for num in nums:
            sumVal += num
            remainder = sumVal%k
            if remainder in prefixSum:
                subArr += prefixSum[remainder]
                prefixSum[remainder] += 1
            else:
                prefixSum[remainder] = 1
        
        return subArr
