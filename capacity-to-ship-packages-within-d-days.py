class Solution:
    def daysTook(self,weights, days, mid):
        daystaken = 0
        shipweight = 0
        for weight in weights:
            shipweight += weight
            if shipweight > mid:
                daystaken += 1
                shipweight = weight
        
        return daystaken+1 <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if self.daysTook(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return right