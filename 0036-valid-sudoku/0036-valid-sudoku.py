class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #iterate through the loop
        for row in range(len(board)):
            #keep track of the numbers on the same row and same column
            rowValues = {}
            columnValues = {}
            
            for column in range(len(board[0])):
                #if not empty add them to the row and column and check if it appears again
                if board[row][column] != '.':
                    if board[row][column] in rowValues:
                        return False
                    else:
                        rowValues[board[row][column]] = True
                        
                if board[column][row] != '.':
                    if board[column][row] in columnValues:
                        return False
                    else:
                        columnValues[board[column][row]] = True
                        
        #iterate through the sub box
        for row in range(3):
            for column in range(3):
                #the sub box
                subboxvalues = {}
                for subrow in range(3):
                    for subcolumn in range(3):
                        if board[subrow+row*3][subcolumn+column*3] != '.':
                            if board[subrow+row*3][subcolumn+column*3] in subboxvalues:
                                return False
                            else:
                                subboxvalues[board[subrow+row*3][subcolumn+column*3]] = True

        #if it ends the loop then it passes
        return True