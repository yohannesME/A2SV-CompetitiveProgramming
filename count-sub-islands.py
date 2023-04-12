class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound( row, col):
            return (0 <= row < len(grid1) and 0 <= col < len(grid1[0]))

        def dfs(row, col):
            nonlocal issubset
            if grid2[row][col] != grid1[row][col]:
                issubset = 0

            #we have now visited hence marked 0
            grid2[row][col] = 0

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid2[new_row][new_col]:
                    dfs(new_row, new_col)

        
        ans = 0
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                #intercept then get island and check subset
                if grid1[row][col] == grid2[row][col] == 1:
                    issubset = 1
                    dfs(row, col)
                    ans += issubset

        return ans