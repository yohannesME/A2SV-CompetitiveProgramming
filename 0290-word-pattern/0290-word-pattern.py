class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        
        
        return len(set(s)) == len(set(pattern)) == len(set(zip_longest(pattern, s)))