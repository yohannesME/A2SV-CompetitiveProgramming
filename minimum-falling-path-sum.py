class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]


        def move(i,j):
            if 0 <= i < n and 0 <= j < n:
                return dp[i][j]
            return float('inf')

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                val = min(move(i+1, j), move(i + 1, j + 1), move(i+1, j - 1))
                if val != float('inf'):
                    dp[i][j] += val
                dp[i][j] += matrix[i][j]


        return min(dp[0])