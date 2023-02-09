class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        decompressed = []
        for index in range(0,N-1,2):
            decompressed += [nums[index+1]]*nums[index]
        
        return decompressed