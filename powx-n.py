class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0:
            n = -n
            return 1/self.myPow(x,n)
        elif not n:
            return 1
        elif n%2:
            return x * self.myPow(x, n-1)
        
        return self.myPow(x*x,n/2)