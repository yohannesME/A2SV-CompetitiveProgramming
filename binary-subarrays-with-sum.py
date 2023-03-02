class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0:1}
        output = 0
        binarysum = 0

        for num in nums:
            binarysum += num
            output += prefix.get(binarysum-goal,0)
            prefix[binarysum] = prefix.get(binarysum, 0) + 1
        
        return output