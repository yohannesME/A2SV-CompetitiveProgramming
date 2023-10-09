class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        @cache
        def backtrack(lvl, bit):
            nonlocal N
            ans = 0

            for i in range(N):
                if bit & (1 << (i+1)) != 0:
                    continue

                bit |= (1 << (i+1))
                for j in range(i+1, N):
                    if bit & (1 << (j+1)) != 0:
                        continue

                    bit |= (1 << (j+1))

                    ans = max(ans, lvl*gcd(nums[i],nums[j]) + backtrack(lvl+1,bit ) )

                    bit &= ~(1 << (j+1))

                bit &= ~(1 << (i+1))
            

            return ans

        return backtrack(1, 0)