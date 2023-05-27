class Solution:
    def tribonacci(self, n: int) -> int:
        def tib(n, memo={}):
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            
            memo[n] = tib(n-1, memo) + tib(n-2, memo) + tib(n-3, memo)
            return memo[n]
        return tib(n)