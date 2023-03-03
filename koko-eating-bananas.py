class Solution:
    def checkPile(self, piles, mid, h):
        hour = 0
        for pile in piles:
            hour += math.ceil(pile/mid)
        return hour <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        
        while left <= right:
            mid = (left+right)//2

            if self.checkPile(piles, mid,h):
                right = mid - 1
            else:
                left = mid + 1

        
        return left