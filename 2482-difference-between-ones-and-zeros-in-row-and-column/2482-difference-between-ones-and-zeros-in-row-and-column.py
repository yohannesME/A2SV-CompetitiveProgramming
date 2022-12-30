class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onesCol = []
        R = len(grid)
        C = len(grid[0])
        #calculate the row sum of all the grids
        for row in grid:
            onesRow.append(sum(row))
        
        #calculate the column by using zip
        for column in zip(*grid):
            onesCol.append(sum(column))
        
        #the array to return the diff
        diff = []
        
        
        #loop throgh the grid and calculate the ones and zeroes for every i,j
        for i in range(len(grid)):
            #calculate a row and then append it to the diff
            row = []
            for j in range(len(grid[0])):
                #zeroes can be found by substracting the ones from the whole row or column size
                diffVal  = onesRow[i] + onesCol[j] - (R-onesRow[i]) - (C-onesCol[j])
                row.append(diffVal)
            diff.append(row)
        
        return diff