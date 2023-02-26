class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                if i == len(word)-1:
                    return ''.join(reversed(word))
                return ''.join(list(reversed(word[:i+1]))+word[i+1:])
        
        return ''.join( word)