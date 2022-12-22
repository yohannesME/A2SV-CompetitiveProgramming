class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        originHash = collections.Counter(s)
        
        #iterate through the list of letter and find one not in the hash
        for letter in t:
            if letter not in originHash:
                return letter
            else:
                if originHash[letter] == 0:
                    return letter
                originHash[letter] -= 1