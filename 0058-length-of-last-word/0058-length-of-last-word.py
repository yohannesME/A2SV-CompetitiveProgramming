class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.rstrip()
        s = s.split()
        
        return len(s[-1])
        
        
        