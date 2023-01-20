class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search to find the middle by which find the square root
        left = 0
        right = x
        while right>=left:
            mid = (left + right)//2

            if mid*mid<=x:
                left = mid+1
            else:
                right = mid-1       
        return right