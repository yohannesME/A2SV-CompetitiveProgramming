class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #check the border for the O and all its adjacent elements as it will not be changed
        #update them to a value other than O then
        #update the rest O to X and return the rest back to O
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))

        def dfs(row, col):
            #we have now visited hence marked 0
            board[row][col] = 'Z'
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                

                if inbound(new_row, new_col) and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)

        rowSize = len(board)
        columnSize = len(board[0])

        #top and bottom 
        #[rowSize-1][--]
        #[0][--]
        for c in range(columnSize):
            if board[rowSize-1][c] == 'O':
                dfs(rowSize-1,c)

            if board[0][c] == 'O':
                dfs(0,c)

        #left and right
        #[--][0]
        #[--][columnSize-1]
        for r in range(rowSize):
            if board[r][columnSize-1] == 'O':
                dfs(r,columnSize-1)

            if board[r][0] == 'O':
                dfs(r,0)

        for r in range(rowSize):
            for c in range(columnSize):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'Z':
                    board[r][c] = 'O'