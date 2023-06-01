class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n for n in range(1, n+1)]


        def move(i,j):
            if 0 <= i < len(triangle) and 0 <= j <= i:
                return dp[i][j]
            return 0

        for i in range(n-1,-1,-1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(move(i+1, j), move(i + 1, j + 1))

        return dp[0][0]