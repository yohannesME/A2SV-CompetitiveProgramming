class Solution:
    def myPow(self, x: float, n: int) -> float:
        # result = 1
        # if n < 0:
        #     for i in range(-n):
        #         result*= x
        #     return 1/result
        # for i in range(n):
        #     result *= x
        # return result
        return pow(x,n)
