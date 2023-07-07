class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return N
        
        up = [0]*N
        down = [0]*N

        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        
        return 1 + max(down[-1], up[-1])