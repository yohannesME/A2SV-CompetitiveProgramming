class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        letter_length = 26
        for i in range(letter_length):
            alphabet[order[i]] = str(i+10)

        before = ""
        for letter in words[0]:
            before+=alphabet[letter]
        for i in range(1,len(words)):
            current = ''
            for letter in words[i]:
                current += alphabet[letter]
            if current >= before:
                before = current
            else:
                return False
        
        return True
