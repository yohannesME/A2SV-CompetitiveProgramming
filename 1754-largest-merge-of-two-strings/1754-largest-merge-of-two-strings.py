class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        #for while two pointer
        #the answer
        merged = []
        
        #length of the arrays
        size1 = len(word1)
        size2 = len(word2)
        
        word2ptr = 0
        
        index = 0
        while index < size1:

            #if equal then try to see ahead
            if word2ptr < size2 and word1[index] == word2[word2ptr]:
                
                firstword = word1[index:]
                secondword = word2[word2ptr:]

                if secondword > firstword:
                    merged.append(word2[word2ptr])
                    word2ptr += 1
                else:
                    merged.append(word1[index])
                    index += 1
                    continue

            #greated lexical value then just add them
            while word2ptr < size2 and word1[index] < word2[word2ptr]:
                merged.append(word2[word2ptr])
                word2ptr += 1
            
            if word2ptr < size2 and word1[index] == word2[word2ptr]:
                continue
            
            merged.append(word1[index])
            index += 1

        
        if word2ptr < size2:
            merged += word2[word2ptr:]
            
        
        return ''.join(merged)


