class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #use negative numbers to change the min heap to a max one
        piles = [-pile for pile in piles]
        heapify(piles)
        #sort the numbers and decrease the largest one
        for _ in range(k):
            value = heappop(piles)
            value += -value//2
            heappush(piles,value)
            
        
        return -sum(piles)