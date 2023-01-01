class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #a new string with the spaces
        string = ''
        
        #keep track of the inserted spaces
        i = 0
        
        for index, letter in enumerate(s):
            
            if i == len(spaces):
                string += s[spaces[-1]+1:]
                break
            if index == spaces[i]:
                i += 1
                string += ' ' + letter
            else:
                string += letter
        
        return string