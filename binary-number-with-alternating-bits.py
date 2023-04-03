class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lastBit = n&1

        while n:
            if  n&1!=lastBit:
                return False
            lastBit ^= 1
            n >>= 1
        return True