class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(num.bit_length()):
            num = num^(1<<i)

        return num