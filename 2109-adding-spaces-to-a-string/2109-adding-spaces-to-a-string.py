class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #a new string with the spaces use space to remove the overhead of altering string
        string = []
        
        #keep track of the inserted spaces
        left = 0
        
        #add all the spaces and create an array             
        for right in range(len(spaces)):
            string.append(s[left:spaces[right]]+' ')
            left = spaces[right]
        
        #add the last substring after the space
        string.append(s[left: len(s)])
        
        #create string from the array and submit
        return ''.join(string)