class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #row column size
        rowSize = len(matrix)
        columnSize = len(matrix[0])
        
        #REVERSE THE COLUMN
        column = 0
        while column < columnSize:
            #last and first element in the row
            rowleft = 0
            rowright = rowSize - 1
            #traverse and swap
            while rowleft < rowright:
                matrix[rowleft][column], matrix[rowright][column] = matrix[rowright][column], matrix[rowleft][column]
                rowleft += 1
                rowright -= 1
            
            column += 1
        
        #used to move to the next diagonal
        diagonal = 0
        
        #first reverse the column
        for row in range(rowSize):
            for column in range(diagonal,columnSize):
                #swap row and column
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
                
            #move to the next diagonal
            diagonal += 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
                
        
        