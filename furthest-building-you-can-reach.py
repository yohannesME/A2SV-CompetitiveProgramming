class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # heap of size ladder
        heap = []
        # brick to get all the values that the ladder can't cover
        brickSize = 0

        #check the value not including the last value 
        for i in range(len(heights)-1):
            # need a brick or a ladder to pass
            if heights[i] < heights[i+1]:
                heappush(heap, heights[i+1]-heights[i] )

                if len(heap) > ladders:
                    brickSize += heappop(heap)

                if brickSize > bricks:
                    return i
        
        return len(heights)-1