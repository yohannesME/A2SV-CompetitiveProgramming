class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        cnt = 0
        count = collections.Counter(nums)
        duplicate = []
        maxnum = len(nums)
        
        for i in range(maxnum*2):
            if count[i] > 1:
                duplicate.extend([i] * (count[i]-1))
    
            elif not count[i] and duplicate:
                cnt += i - duplicate.pop()
        return cnt
