class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort the people to create the optimal match
        people.sort()
        
        #create the pointers used to traverse
        leftBound = 0
        rightBound = len(people)-1
        
        #the output
        total = 0
        
        
        while leftBound <= rightBound:
            #one person just add another bot
            if leftBound == rightBound:
                total += 1
                break
            #if limit reached by either add another bot
            if people[leftBound] == limit:
                total += 1
                leftBound += 1
                
            if people[rightBound] == limit:
                total += 1
                rightBound -= 1
            
            #if addition of the people weight is less than or equal to limit add one boat else add two for each
            if people[rightBound] + people[leftBound] <= limit:
                total += 1
                leftBound += 1
                rightBound -= 1
            else:
                rightBound -= 1
                total += 1
                
        return total
            
            
                      
                    
        