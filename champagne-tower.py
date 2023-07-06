class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = query_row + 1
        dp = [[0]*n for n in range(1, n+1)]

        def move(i,j):
            if 0 <= i < len(dp) and 0 <= j <= i and dp[i][j] > 1:
                return dp[i][j] - 1
            return 0

        dp[0][0] = poured

        for i in range(1,n):
            for j in range(len(dp[i])):
                dp[i][j] = (move(i-1, j)+ move(i-1, j-1))/2

        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1