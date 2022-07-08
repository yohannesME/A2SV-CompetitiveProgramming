class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            s = [i for i in s]
            s.reverse()
            s = ''.join(s)
            return s
        def invert(s):
            invr = ''
            for i in range(len(s)):
                if s[i] == "0":
                    invr += "1"
                else:
                    invr += "0"
            return invr
        @functools.cache
        def func(num):
            if num == 1:
                return "0"
            else:
                return func(num-1)+"1"+reverse(invert(func(num-1)))
        bits = func(n)
        print(bits)
        return bits[k-1]
