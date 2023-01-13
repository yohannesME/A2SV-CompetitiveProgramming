class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #create a hash map to keep track of the diagonal elements
        diagonal = {}
        
        #iterate through the matrix
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                #add the diagonal elements to the hashmap
                if row - column not in diagonal:
                    diagonal[row-column] = matrix[row][column]
                 
                #when encountering a diagonal  check if they are the same
                else:
                    if diagonal[row-column] != matrix[row][column]:
                        return False
        
        #if the loop end then we know they are the same
        return True