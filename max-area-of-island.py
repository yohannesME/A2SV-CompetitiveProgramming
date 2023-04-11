class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(row, col):
            # base case
            if grid[row][col] == 0 or grid[row][col] in visited:
                return 0

            visited[row][col] = True


            area = 1
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                

                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    area += dfs(new_row, new_col)
            return area
        
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ans = max(ans, dfs(row, col))
        
        return ans