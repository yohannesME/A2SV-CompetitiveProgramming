class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        numRows -= 1
        pascal = [[1]]
        
        while numRows > 0:
            row = [1]
            if len(pascal[-1]) > 1:
                for i in range(len(pascal[-1])-1):
                    row.append(pascal[-1][i]+pascal[-1][i+1])
            row.append(1)
            pascal.append(row)
            
            numRows -= 1
            
        return pascal
            