class Solution:
    def isPalindrome(self, x: int) -> bool:
        return ''.join(reversed(list(str(x))))==str(x)
        