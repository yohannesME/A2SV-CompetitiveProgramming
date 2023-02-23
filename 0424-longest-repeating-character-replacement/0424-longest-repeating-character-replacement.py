class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #inial values used sliding window, length, answer
        longestRep = 0 
        N = len(s)
        rightBound = 0
        leftBound = 0
        
        #count the occurance
        letterCount = defaultdict(int)
        
        #until we reach the point we have no more k moves we check and update longest
        while rightBound < N:
            letterCount[s[rightBound]] += 1
            
            maxRep = 0
            for letter in letterCount:
                maxRep = max(maxRep, letterCount[letter])
            
            if rightBound - leftBound + 1 - maxRep > k:
                letterCount[s[leftBound]] -= 1
                leftBound += 1
            else:
                longestRep = max(longestRep,rightBound - leftBound + 1 )
            
            rightBound += 1

        return longestRep