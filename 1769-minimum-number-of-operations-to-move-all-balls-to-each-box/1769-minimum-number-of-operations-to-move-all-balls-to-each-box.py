class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #all the occurances of ones
        ones = []
        
        #the output
        output = []
        
        #populate the one index
        for index,binary in enumerate(boxes):
            if binary == '1':
                ones.append(index)
        
        #loop through the boxes
        for index in range(len(boxes)):
            #take the number of operation by taking the distance from the current index to the position of the other ones
            operation = 0
            for one in ones:
                operation += abs(one-index)
            
            output.append(operation)
        
        return output
