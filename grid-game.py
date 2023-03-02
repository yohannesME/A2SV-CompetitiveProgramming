class Solution:
    # #create a prefix sum in a reverse order
    # def createPrefix(self, grid, N):
    #     gridPrefix = [[0],[0]]

    #     for i in range(N-1,-1,-1):
    #         gridPrefix[0].append(gridPrefix[0][-1] + grid[0][i] )
    #         gridPrefix[1].append(gridPrefix[1][-1] + grid[1][i] )
        
    #     for i in range(len(gridPrefix)):
    #         gridPrefix[i] = gridPrefix[i][::-1]
    #         gridPrefix[i].pop()
    #     return gridPrefix

    # def gridGame(self, grid: List[List[int]]) -> int:
    #     N = len(grid[0])
    #     gridPrefix = self.createPrefix(grid, N)

    #     #first robot maximum number turn to zero
    #     grid[0][0] = 0
    #     column = 0
    #     row = 0
    #     while column < N-1 and gridPrefix[row][column+1] > gridPrefix[row+1][column]:
    #         grid[row][column+1] = 0
    #         column += 1
        
    #     row += 1  
    #     while column < N:
    #         grid[row][column] = 0
    #         column += 1
    #     print(gridPrefix)
        
    #     #the second robot collect maximum number of point left from the first robot
    #     gridPrefix = self.createPrefix(grid, N)
    #     column = 0
    #     row = 0
    #     answer = 0
    #     while column < N-1 and gridPrefix[row][column+1] > gridPrefix[row+1][column]:
    #         answer += grid[row][column+1]
    #         column += 1
        
    #     row += 1  
    #     while column < N:
    #         answer += grid[row][column]
    #         column += 1
        
    #     print(grid, gridPrefix)

    #     return answer

    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        bottom= 0
        answer = float('inf')

        for grid0, grid1 in zip(grid[0], grid[1]):
            top -= grid0
            answer = min(answer, max(top, bottom))
            bottom += grid1
            print(grid0, grid1, answer)
        return answer