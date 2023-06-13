class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        thesame = 0
        for column in zip(*grid):
            column = list(column)
            for row in grid:
                if column == row:
                    thesame += 1
        
        
        return thesame