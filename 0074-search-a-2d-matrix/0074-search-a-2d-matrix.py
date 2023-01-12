class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #the dimension of the matrix
        rowSize = len(matrix)
        columnSize = len(matrix[0])
        
        
        for  row in range(rowSize):
            if matrix[row][-1] >= target:
                
                #as the elements are sorted we can use binary search to find the element
                left = 0
                right = columnSize - 1
                
                while left <= right:
                    
                    mid = (left+right)//2
                    
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
        
        #if the value is greater
        return False
                
                    
            