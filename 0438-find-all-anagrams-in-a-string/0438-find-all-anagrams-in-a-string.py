class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLength = len(s)

        lagging = 0 
        fast = 0
        
        #number of encountered letters
        lettersHash = Counter(p)
        
        #acutally encounter
        countered = {}

        #index of the anagram encounter
        output = []
        
        #find the window size
        for i in range(len(p)):
            #if string is greater than anagram collection them return [empty]
            if fast > sLength-1:
                return []
           
            #calculate count of current string
            countered[s[fast]] = countered.get(s[fast],0)+1
            fast += 1
        #as range end fast is one app so decrease that
        fast -= 1


        while fast < sLength:
            #check if the letterHash original string is equal to the newly found one
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

            #remove the element at the edge if the count is 1
            if countered[s[lagging]] == 1:
                del countered[s[lagging]]
            else:
                countered[s[lagging]] -= 1
            lagging += 1
            
            fast += 1
            #we increase fast check the index out of bound
            if fast < sLength:
                countered[s[fast]] = countered.get(s[fast],0) + 1
                


        return output
            
            