class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        ans = 0
        bitMask = []
        for index,word in enumerate(words):
            mask = 0
            for letter in word:
                mask |= 1 << ord(letter) - 97
            bitMask.append(mask)

        #the bit mask will not have a value that will intercect so the & will be zero
        for i in range(N):
            for j in range(i+1, N):
                if bitMask[i] & bitMask[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
                
        return ans