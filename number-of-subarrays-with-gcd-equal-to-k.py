class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        N = len(nums)  
        subArr = 0

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        for i in range(N):
            currentgcd = nums[i]
            for j in range(i, N):
                currentgcd = gcd(currentgcd, nums[j])
                if currentgcd == k:
                    subArr += 1

        return subArr