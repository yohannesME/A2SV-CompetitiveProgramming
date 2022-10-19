class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        l,r = 0,len(tokens)-1
        score = 0
        
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
            elif score > 0 and l != r:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return score
                    
