class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numbers = set([str(i) for i in range(1,10)])
        rowMap = [set() for i in range(9)]
        columnMap = [set() for i in range(9)]
        boxMap = [set() for i in range(9)]
        for row in range(9):
            for column in range(9):
                if board[row][column] != '.':
                    rowMap[row].add(board[row][column])
                    columnMap[column].add(board[row][column])
        #iterate through the sub box
        index = -1
        for row in range(3):
            for column in range(3):
                index += 1
                #sub box
                for subrow in range(3):
                    for subcolumn in range(3):
                        if board[subrow+row*3][subcolumn+column*3] != '.':
                            boxMap[index].add(board[subrow+row*3][subcolumn+column*3])
        
        def find():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        return (r,c)
            return None
        
        def backtrack():
            emptyVal = find()
            if not emptyVal:
                return True
            else:
                row, col = emptyVal

            for number in range(1, 10):
                if str(number) not in (rowMap[row] | columnMap[col] | boxMap[(row//3)*3+col//3]):
                    rowMap[row].add(str(number))
                    columnMap[col].add(str(number))
                    boxMap[(row//3)*3+col//3].add(str(number))
                    board[row][col] = str(number)

                    if backtrack():
                        return True

                    rowMap[row].remove(str(number))
                    columnMap[col].remove(str(number))
                    boxMap[(row//3)*3+col//3].remove(str(number))
                    board[row][col] = '.'

            return False


                
        backtrack()