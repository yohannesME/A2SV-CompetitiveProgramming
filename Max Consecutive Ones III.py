class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end = 0,0
        longest = 0
        temp = k
        count = 0
        while end < len(nums):
            while end < len(nums) and (temp > 0 or nums[end] == 1):
                if nums[end]==1:
                    count += 1
                    end += 1
                else:
                    temp -= 1
                    count += 1
                    end += 1
            longest = max(longest, count)

            if nums[start] == 1:
                count -= 1
            else:
                if start == end:
                    end += 1
                else:
                    temp += 1
                    count -= 1
            start += 1
        return longest
