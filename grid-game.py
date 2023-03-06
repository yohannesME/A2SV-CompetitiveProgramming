class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        bottom= 0
        answer = float('inf')

        for grid0, grid1 in zip(grid[0], grid[1]):
            top -= grid0
            answer = min(answer, max(top, bottom))
            bottom += grid1
        return answer