class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(1,1),(-1,-1), (1,-1),(-1,1)]
        queue = deque([(0,0,1)])

        def inbound(row, col):
            nonlocal n
            return (0 <= row < n and 0 <= col < n)

        while queue:
            row, col, pathLen = queue.popleft()
            if row == col == n-1:
                return pathLen

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, pathLen+1))
                    grid[new_row][new_col] = 1

        return -1