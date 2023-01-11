class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #first create a set to contain the intercept
        intercept = {}
        
        #output
        output = []
        
        #find the letters in the first word to  use as a starter
        for letter in words[0]:
            intercept[letter]  = intercept.get(letter, 0) + 1
        
        #begin from the second word and check their letter
        for index in range(1,len(words)):
            #create a new intercept that matches with the coming word
            newIntercept = {}
            for letter in words[index]:
                if letter in intercept:
                    if intercept[letter] > 0:
                        newIntercept[letter] = newIntercept.get(letter,0) + 1
                    intercept[letter] -= 1
            
            #replace the intercept with the new Intercept 
            intercept = newIntercept
        
        #add all the letters as much as their apperance aka count
        for letter, count in intercept.items():
            for i in range(count):
                output.append(letter)
        
        #return the list version of the array
        return output