class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        #check if the input grid is less than 3x3
        #input the size of the row and column
        rowSize = len(grid)
        columnSize = len(grid[0])
        
        if rowSize < 3 or columnSize < 3:
            return 0
        
        #hold the account of magic squares
        magicSquares = 0
        
        #check if a 3x3 matrix is magic square
        def validateMagicSquare(row,column):
            #check each side and diagonal sum value to be equal by accomulating them in the hashmap
            sumTracker = defaultdict(int)
            diagonalSumTracker = defaultdict(int)

            #check if a number is repeated
            numberTracker = {}
            
            for magicrow in range(row,3+row):
                for magiccolumn in range(column, 3+column):
                    #check if already encountered
                    if grid[magicrow][magiccolumn] in numberTracker:
                        return 0
                    #check if number is greater than 9 or less than 1
                    if grid[magicrow][magiccolumn] > 9 or grid[magicrow][magiccolumn] < 1:
                        return 0
                    
                    #add the current number as encountered
                    numberTracker[grid[magicrow][magiccolumn]] = True

                    #accomulate the sum
                    sumTracker[str(magicrow)+'r'] += grid[magicrow][magiccolumn]
                    sumTracker[str(magiccolumn)+'c'] += grid[magicrow][magiccolumn]

                    if row-column == magicrow-magiccolumn:
                        diagonalSumTracker[str(row-column)+'l'] += grid[magicrow][magiccolumn]
                    if row+column+2 == magiccolumn + magicrow:
                        diagonalSumTracker[str(row+column+2)+'r'] += grid[magicrow][magiccolumn]

            #create a set of all the sum values all sides and diagonals
            allSum = set(list(sumTracker.values()) + list(diagonalSumTracker.values()))

            #check if the sum are all equal
            if len(allSum) == 1:
                return 1
            else:
                return 0

        
        #iterate over the array 3x3 at a time
        for row in range(rowSize-3+1):
            for column in range(columnSize -3+1):
                magicSquares += validateMagicSquare(row,column)

        
        return magicSquares