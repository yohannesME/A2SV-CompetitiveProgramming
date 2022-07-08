class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isPower(n):
            if n <= 0:
                return False
            elif n % 3==0:
                return isPower(n/3)
            elif n ==1:
                return True
            else:
                return False
        return isPower(n)
