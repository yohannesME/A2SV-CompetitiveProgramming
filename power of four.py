class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def isPower(n):
            if n <= 0:
                return False
            elif n % 4==0:
                return isPower(n/4)
            elif n ==1:
                return True
            else:
                return False
        return isPower(n)        
