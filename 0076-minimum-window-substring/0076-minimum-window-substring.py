class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sN = len(s)
        tN = len(t)
        
        if sN < tN:
            return ''
        
        tCount = Counter(t)
        sCount = defaultdict(int)
        
        minimumWindow = [float('inf'), sN, sN]

        leftBound  = 0
        rightBound = 0
        
        while rightBound < sN+1:
            checker = True
            for letter in tCount:
                if tCount[letter] > sCount[letter]:
                    checker = False

            if checker:
                if minimumWindow[0] > rightBound - leftBound + 1:
                    minimumWindow[0] = rightBound - leftBound + 1
                    minimumWindow[1] = leftBound
                    minimumWindow[2] = rightBound
                    
                    
                sCount[s[leftBound]] -= 1
                leftBound += 1
            else:
                if rightBound < sN:
                    sCount[s[rightBound]] += 1

                rightBound += 1
                
        if minimumWindow[1] == sN:
            return ''
        return s[minimumWindow[1]:minimumWindow[2]]
            
                
            