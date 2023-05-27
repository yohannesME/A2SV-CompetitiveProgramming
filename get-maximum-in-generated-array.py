class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # memo = {}
        # def dp(i):
        #     # print(i, memo)
        #     if i in memo:
        #         return memo[i]

        #     if i < 2:
        #         return i
            
        #     if i & 1:
        #         memo[i] = dp(i//2) + dp(i//2 + 1)
        #         return memo[i]
        #     else:
        #         memo[i] = dp(i//2)
        #         return memo[i]

        # # if n & 1 != 1:
        # #     n -= 1       
        # return dp(n)

        if n < 2:
            return n

        nums = [0]*(n+1)
        nums[1] = 1
        maximum = 1

        i = 1
        while i <= n:
            double = i*2
            if double <= n:
                nums[double] = nums[i]
                maximum = max(maximum, nums[double])
            else:
                break
            if double + 1 <= n:
                nums[double + 1] = nums[i] + nums[i + 1]
                maximum = max(maximum, nums[double + 1])
            else:
                break
            
            i += 1

        return maximum