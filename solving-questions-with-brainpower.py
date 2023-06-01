class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * N
        maximum = 0

        for i in range(N-1,-1,-1):
            point, brainpower = questions[i]
            brainpower += 1

            dp[i] = max(point + (dp[i + brainpower] if i + brainpower < N else 0), (dp[i+1] if i+1 < N else 0))

            maximum = max(maximum, dp[i])
        
        return maximum