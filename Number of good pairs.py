class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = set(nums)
        num = list(num)
        count = [0]*len(num)
        for n in nums:
            for i in range(len(num)):
                if (num[i] == n):
                    count[i] = count[i] +1
        result = 0
        for c in count:
            result = result + (c*(c-1))/2
        return int(result)
