class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        ##!!!O(N^2) TIME LIMITED EXCEEDS
#         #SELECTION SORT BUT RATHER THAN MOVING THE ELEMENT JUST REPLACE IT
#         N = len(arr)
#         for i in range(N-1):
#             #find the maximum element in the range of numbers greater than i
#             arr[i] = max(arr[i+1:])
        
#         #the last element will be -1
#         arr[-1] = -1
        
        N = len(arr)
        maximumElements = []
        
        for index in range(N):
            maximumElements.append([arr[index],index])
            
        #sort the element depending on the value
        maximumElements.sort(reverse=True)
        
        #keep track of the element put
        putFrom = 0
        for value, index in maximumElements:
            if index == 0:
                continue

            #put the maximum element in the range that the elements 
            if index >= putFrom:
                for i in range(putFrom, index):
                    arr[i] = value
                putFrom = index
            
        #the last element is always -1
        arr[-1] = -1
    
        return arr