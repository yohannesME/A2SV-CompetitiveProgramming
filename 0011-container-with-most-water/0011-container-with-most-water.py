class Solution:
    def maxArea(self, height: List[int]) -> int:
        #left and right bounds
        leftBound = 0
        rightBound = len(height)-1
        
        #output
        result = 0
        
        while leftBound < rightBound:
            #result is maximum container the range found by the bound substraction
            #and the minimum height that which can carry water
            result = max(result, (rightBound-leftBound)*min(height[rightBound],height[leftBound]))
            
            #move from the smallest bound
            if height[leftBound] > height[rightBound]:
                rightBound -= 1
            else:
                leftBound += 1
        
        return result
        