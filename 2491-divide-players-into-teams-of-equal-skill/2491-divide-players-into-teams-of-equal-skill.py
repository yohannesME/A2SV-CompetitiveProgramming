class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #left and right pointers starting from the second iteration
        leftBound = 0+1
        rightBound = len(skill)-1-1
        
        #sort the array to find sum combo
        skill.sort()     
        
        #output created with the first combo multiple
        output = skill[leftBound-1] * skill[rightBound+1]

        #hold the skill all will have the same of
        skillValue = skill[leftBound-1] + skill[rightBound+1]
        
        
        while leftBound <= rightBound:
            #check all have the same skill combo
            if skillValue == skill[leftBound] + skill[rightBound]:
                #add their skill multiple
                output += skill[leftBound] * skill[rightBound]
                
                #move the pointers
                leftBound += 1
                rightBound -= 1
            else:
                #if encountered skill that are not equal to other skill combo return -1
                return -1
        
        #passed so return output
        return output
        