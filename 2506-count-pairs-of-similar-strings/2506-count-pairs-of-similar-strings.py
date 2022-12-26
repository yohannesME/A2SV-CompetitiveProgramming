from collections import defaultdict
from itertools import permutations

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        #create ordered hash element of the words that are coverted to set
        wordletters = defaultdict(list)
        output = 0
        
        #iterate through the word and create a array of the occurence of the letters in the 
        #array and sort them to make the hash key the same
        for index,word in enumerate(words):
            #remove duplication
            wordset = list(set(word))
            wordset.sort()
            
            wordletter = ''.join(wordset)
            
            wordletters[wordletter].append(index)

        #check if occurence is more than one and add the possible arrangement
        for occur in wordletters.values():
            output += self.possiblePair(len(occur))


        return output
    
    
    def possiblePair(self,n):

        result = 0
        for i in range(1,n):
            result += i

        return result