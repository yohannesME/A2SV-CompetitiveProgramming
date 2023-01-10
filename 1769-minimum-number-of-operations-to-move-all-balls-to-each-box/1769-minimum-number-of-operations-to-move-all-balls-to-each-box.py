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
        
        for index in range(len(boxes)):
            operation = 0
            for one in ones:
                operation += abs(one-index)
            
            output.append(operation)
        
        return output