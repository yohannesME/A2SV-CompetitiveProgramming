class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        n1 = len(word1)
        n2 = len(word2)
        # take the largest array to iterate as much as that array
        large = n1 if n1 > n2 else n2
        
        #first input word1 and then word2 in the input
        for i in range(large):
            if i < n1:
                output += word1[i]
            if i < n2:
                output += word2[i]
        return output