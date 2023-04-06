class Solution:
    def minSteps(self, n: int) -> int:
        # if n == 1:
        #     return 0

        # def dp(total=1 , prevCopy=1):
        #     nonlocal n
        #     if total > n:
        #         return 0
        #     elif total == n:
        #         return 1
        #     else:
        #         copy = 0
        #         paste = 0
        #         if total == prevCopy:
        #             paste = dp(total+prevCopy, prevCopy)
        #         else:
        #             paste = dp(total+prevCopy, prevCopy)
        #             copy = dp(total,total)

        #         if copy != 0 and paste != 0:
        #             return 1+ min(copy, paste)
        #         elif  copy != 0 or paste != 0:
        #             return 1+max(copy,paste)
        #         else:
        #             return 0
        
        # return dp()
        result = 0
        d = 2

        while n > 1:
            while n%d ==0:
                result += d
                n //= d
            d += 1
        return result