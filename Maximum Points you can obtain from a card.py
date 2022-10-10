class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r = 0, len(cardPoints)-k
        total = sum(cardPoints[r:])
        maxPoint = total
        while r < len(cardPoints):            
            total += cardPoints[l]
            l += 1
            total -= cardPoints[r]
            r += 1
            maxPoint = max(maxPoint, total)
            print(total)
            
        return maxPoint
