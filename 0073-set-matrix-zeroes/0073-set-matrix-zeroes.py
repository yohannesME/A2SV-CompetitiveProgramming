class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow = {}
        zeroColumn = {}
        
        #the grid
        rowSize = len(matrix)
        columnSize = len(matrix[0])
        
        for row in range(rowSize):
            for column in range(columnSize):
                if matrix[row][column] == 0:
                    zeroRow[row] = True
                    zeroColumn[column] = True
                    
        
        for row in range(rowSize):
            for column in range(columnSize):
                if row in zeroRow:
                    matrix[row][column] = 0
                elif column in zeroColumn:
                    matrix[row][column] = 0
            
        
        
       