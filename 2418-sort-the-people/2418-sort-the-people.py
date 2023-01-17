class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        #sort the name as well when we are sorting the height
        
        heightSize = len(heights)
        for i in range(heightSize):
            for j in range(0,heightSize-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j+1], names[j] = names[j], names[j+1]

        return names
            