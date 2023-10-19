class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Length = len(s1)
        s2Length = len(s2)
        
        #check if permutation is bigger
        if s1Length > s2Length:
            return False
    
        #the count of permutation we look for
        s1Count = Counter(s1)
        #recorder to check if we find it
        s2Counter = {}
        
        #right and left Bound
        rightBound = s1Length-1
        leftBound = 0
        
        #added the first window
        for index in range(s1Length):
            s2Counter[s2[index]] = s2Counter.get(s2[index],0) + 1

        #check to see each one moving the window
        while rightBound < s2Length:
            if s1Count == s2Counter:
                return True

            if s2Counter[s2[leftBound]] == 1:
                del s2Counter[s2[leftBound]]
            else:
                s2Counter[s2[leftBound]] -= 1
                
            leftBound += 1
                
            rightBound += 1
            if rightBound < s2Length:
                s2Counter[s2[rightBound]] = s2Counter.get(s2[rightBound],0) + 1
        
        return False