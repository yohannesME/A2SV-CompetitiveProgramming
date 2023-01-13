class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #the movement of the spiral 
        [right, down,left,up] = [(0,1), (1,0), (0,-1), (-1,0)]
        
        #the answer 
        spiral = []
        
        
        #the bounds of the matrix nxm
        rowSize = len(matrix)
        columnSize = len(matrix[0])
        
                
        #out index for matrix traversal
        row = 0
        column = 0
        
        #traverising while going in spiral
        def traverse(direction):
            nonlocal row,column
            #check ahead if the movement if out of bound,
            if not self.isOutOfBound(row+direction[0],column+direction[1], rowSize,columnSize):
                #check ahead if the movement is going toward visited node
                if not self.isVisited(matrix[row+direction[0]][column+direction[1]]):
                    row += direction[0]
                    column += direction[1]
                    
                    spiral.append(matrix[row][column]) 

                    #visited node changed to -101
                    matrix[row][column]  = -101
                    return True
                else:
                    #visited
                    return False
            else:
                #out of bound
                return False        
        

        
        #add the first spiral element
        spiral.append(matrix[row][column])
        
        #mark the first element as visited
        matrix[row][column] = -101

        while True:
            #right -> down -> left -> up-> repeat
            #if not all then your done
            if traverse(right):
                while traverse(right):
                    continue
            elif traverse(down):
                while traverse(down):
                    continue                
                continue
            elif traverse( left):
                while traverse(left):
                    continue
                continue
            elif traverse(up):
                while traverse(up):
                    continue
                continue
            else:
                break

        
        return spiral
                    
        
        
        

                
    
    
    
    
    #check if the element is out of bound
    def isOutOfBound(self, row, column, rowSize, columnSize):
        return row < 0 or row == rowSize or column < 0 or column == columnSize
                
    #check if already visited element
    def isVisited(self, currentValue):
        return currentValue == -101
    
  