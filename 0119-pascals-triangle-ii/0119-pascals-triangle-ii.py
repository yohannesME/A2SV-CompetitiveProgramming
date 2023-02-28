class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        else:
            row = [1]
            #get the last rowIndex recursively
            triangle = self.getRow(rowIndex-1)
            for i in range(len(triangle)-1):
                row.append(triangle[i]+triangle[i+1])
            row.append(1)
            return row