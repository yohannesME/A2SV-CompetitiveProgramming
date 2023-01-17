class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        #sort the name as well when we are sorting the height
        
        heightSize = len(heights)
        for i in range(heightSize):
            for j in range(i,heightSize):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
        
        return names
            