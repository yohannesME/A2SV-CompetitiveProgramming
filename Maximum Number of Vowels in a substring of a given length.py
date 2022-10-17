class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a':True, 'e':True, 'i':True, 'o':True, 'u':True}
        
        count = 0
        maxCount = 0
        lagging, fast = 0,0
        
        for i in range(k):
            if s[fast] in vowels:
                count += 1
            fast += 1
        fast -= 1
        
        while fast < len(s):
            #maximum of the count
            maxCount = max(maxCount,count)
            
            if s[lagging] in vowels:
                count -= 1
            lagging += 1
            
            fast += 1
            if fast < len(s) and s[fast] in vowels:
                count += 1
        
        return maxCount
            
            
            
        
        
        
