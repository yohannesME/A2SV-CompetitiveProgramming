class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        #the output 
        maxLocal = []

        #the matrix is nxn
        matrixSize = len(grid)
        

        #iterate through the grid but 3 at a time
        for row in range(matrixSize-3+1):
            #hold each row max local
            maxLocalRow = []
            
            
            for column in range(matrixSize-3+1):
                #for each 3x3 matrix iterate and find the max
                maximum = 0
                for r in range(3):
                    for c in range(3):
                        maximum = max(maximum, grid[r+row][c+column])
                maxLocalRow.append(maximum)
            maxLocal.append(maxLocalRow)
        
        
        return maxLocal
                    