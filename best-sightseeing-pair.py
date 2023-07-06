class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        answer = 0
        maxval = 0

        for i, val in enumerate(values):
            answer = max(answer, maxval + val - i)
            maxval = max(maxval, val + i)
        
        return answer