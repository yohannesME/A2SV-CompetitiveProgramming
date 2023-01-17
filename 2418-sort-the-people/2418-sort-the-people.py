class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        #sort the name as well when we are sorting the height
        
#         #BUBBLE SORT
#         heightSize = len(heights)
#         for i in range(heightSize):
#             for j in range(0,heightSize-1-i):
#                 if heights[j] < heights[j+1]:
#                     heights[j], heights[j+1] = heights[j+1], heights[j]
#                     names[j+1], names[j] = names[j], names[j+1]

#         return names
            
        
#         #SELECTION SORT
        heightSize = len(heights)
        for i in range(heightSize):
            #find the maximum number in the array and record its index
            maximum = heights[i]
            index = i
            
            #iterate over the array and record the largest element index
            for j in range(i+1,heightSize):
                if heights[j] > maximum:
                    maximum = heights[j]
                    index = j
                    
            #check if more larger element was found     
            
            heights[i], heights[index] = heights[index], heights[i]
            names[i], names[index] = names[index], names[i]

        return names
                    
         
        
    
    
            