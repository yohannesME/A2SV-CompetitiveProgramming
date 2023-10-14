class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        mod = 10**9 + 7

        needlehash = 0
        haystackhash = 0

        if m > n:
            return -1

        for i in range(m):
            needlehash += (ord(needle[i]) - 97 + 1)*26**(m-1-i)
            haystackhash += (ord(haystack[i]) - 97 + 1)*26**(m-1-i)
        
        if needlehash%mod == haystackhash%mod:
            return 0

        left = 0
        right = 0
        j = 1
        
        for i in range(m, n):
            haystackhash -= ((ord(haystack[j-1]) - 97 + 1) * 26**(m-1))
            haystackhash *= 26
            haystackhash += ord(haystack[i]) - 97 + 1

            if haystackhash % mod == needlehash % mod:
                return j
            j += 1
        return -1