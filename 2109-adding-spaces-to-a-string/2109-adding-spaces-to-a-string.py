class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #a new string with the spaces use space to remove the overhead of altering string
        string = []
        
        #keep track of the inserted spaces
        i = 0
        
        for index, letter in enumerate(s):
            #when done adding the space add what is left and break
            if i == len(spaces):
                string.append(s[spaces[-1]+1:])
                break
            if index == spaces[i]:
                i += 1
                string.append(' ' + letter)
            else:
                string.append(letter)
        
        return ''.join(string)