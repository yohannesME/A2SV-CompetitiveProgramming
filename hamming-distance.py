class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x^y
        diffCount = 0
        while diff > 0:
            diffCount += (diff&1)
            diff >>= 1
        return diffCount