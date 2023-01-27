class Solution:
    def compress(self, chars: List[str]) -> int:
        #non repeating count
        index = 0
        
        N = len(chars)
        
        #two pointers to count the repetition
        current = 0
        lookahead = 0
        

        #get the occurance of all character then add their count to the array
        while current < N and lookahead < N:
            #look for different value
            while lookahead < N and chars[current] == chars[lookahead]:
                lookahead += 1

            #add the encountered count value
            if lookahead < N+1 and current < N:
                chars[index] = chars[current]
                index += 1
                
                
                letterCount = str(lookahead - current)
                #only if it is greater than one and if two digit split it 12 will be 1,2
                if letterCount > '1':
                    for num in letterCount:
                        chars[index] = num
                        index +=1
                #update current value
                current = lookahead

        #no need to add + 1 to the last index  since it does that after every op
        return index