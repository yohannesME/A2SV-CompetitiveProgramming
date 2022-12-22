class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        output =[ float('inf'),-1]
        #distance between points is radical (x2-x1)**2 + (y2-y1)**2
        for i,coord in enumerate(points):
            if coord[0] == x or coord[1] == y:
                distance = abs(coord[0]-x) + abs(coord[1]-y)
                #update output if distance is accurate and is less than output
                if distance < output[0]:
                    output = [distance, i]
        return output[1]
            
        