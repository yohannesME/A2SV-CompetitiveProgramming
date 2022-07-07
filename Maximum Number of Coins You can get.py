class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)

        total = 0;

        while(len(piles) > 0):
            total += piles[1]
            piles.pop()
            del piles[0]
            del piles[0]
        return total;
        
