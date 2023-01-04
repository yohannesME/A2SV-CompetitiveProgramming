class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        #output declaration
        output = []
        
        #split the word by space and zip the words veritcally 
        #zip_longest to constitute words that have larger length
        for vertical in zip_longest(*s.split(), fillvalue=' '):

            #replace None with ' ' for words that are places when the word is long (None, None, None, 'T', None, None)
            vertical = list(map(lambda word: word if word != None else ' ', vertical))

            #change the tuple returned into a string
            word = ''.join(vertical)
            
            #remove space from the end of the string if None was replaced by it
            word = word.rstrip()
            
            #append to input
            output.append(word)
            
        return output
        