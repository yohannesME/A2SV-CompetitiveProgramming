class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLength = len(s)

        lagging, fast = 0,0
        
        lettersHash = {}

        for letter in p:
            lettersHash[letter] = lettersHash.get(letter,0)+1
        
        countered = {}

        output = []
        
        for i in range(len(p)):
            if fast > sLength-1:
                return []
            countered[s[fast]] = countered.get(s[fast],0)+1
            fast += 1
        
        fast -= 1

        while fast < sLength:
            checker = True
            if len(lettersHash) == len(countered):
                for letter in lettersHash:
                    if letter in countered:
                        if countered[letter]!=lettersHash[letter]:
                            checker = False
                            break
                    else:
                        checker = False
                        break
            else:
                checker = False
            
            if checker:
                output.append(lagging)
            # print(countered, lagging,fast)
            if countered[s[lagging]] == 1:
                del countered[s[lagging]]
            else:
                countered[s[lagging]] -= 1
            lagging += 1
            
            fast += 1
            if fast < sLength:
                countered[s[fast]] = countered.get(s[fast],0) + 1
                


        return output
            
   
