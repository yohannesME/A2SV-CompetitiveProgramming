class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Convert to Negative to use in heapq
        stones = [-stone for stone in stones]

        #Heapify and create heap
        heapify(stones)

        # If We have more than one element in the do the required task
        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)

            if stone1 != stone2:
                heappush(stones,stone1-stone2)
        
        # If we have one element left in the heap return that else return 0
        if stones:
            return -stones[0]
        return 0