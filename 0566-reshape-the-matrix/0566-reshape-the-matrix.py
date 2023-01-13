class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        #size of the original matrix
        rowSize = len(mat)
        columnSize = len(mat[0])

        #if reshape is not possible
        if rowSize*columnSize != r*c:
            return mat
                
        #the answer the resahped matrix
        reshaped = [[0]*c for i in range(r)]
        
        #temporary flatten the matrix
        flattened = []
        
        #iterate through the matrix and them in 1d array
        for row in range(rowSize):
            for column in range(columnSize):
                flattened.append(mat[row][column])
        
        #add the flattened array to the reshaped matrix
        index = 0
        for row in range(r):
            for column in range(c):
                reshaped[row][column ] = flattened[index]
                index += 1
        
        return reshaped