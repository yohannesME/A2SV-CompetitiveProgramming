class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        cardCount = list(Counter(deck).values())
        partition = gcd(*cardCount)

        if partition == 1:
            return False

        return True