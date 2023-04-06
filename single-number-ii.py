class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # one = 0
        # two = 0
        # for num in nums:
        #     one = (one^num) & (~two)
        #     two = (two^num) & (~one)
        # return one

        for i in range(len(nums)):
            nums[i] += 2**31
            
        ans = 0
        for i in range(32):
            bitCount = 0
            for num in nums:
                if num & (1 << i) != 0:
                    bitCount +=1

            ans |= ((bitCount%3) << i)

        return ans-2**31