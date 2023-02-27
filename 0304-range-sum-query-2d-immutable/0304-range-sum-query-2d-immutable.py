class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        #create the prefix sum
        for matrx in matrix:
            self.prefix.append([matrx[0]])
            for i in range(1,len(matrx)):
                self.prefix[-1].append(self.prefix[-1][-1] + matrx[i])        

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #add the values
        add = 0
        for i in range(row2-row1 + 1):
            add += self.prefix[row1 + i][col2] - self.prefix[row1 + i][col1] + self.matrix[row1 + i][col1]
        return add


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)