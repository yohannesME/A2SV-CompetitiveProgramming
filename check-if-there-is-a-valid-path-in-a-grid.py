class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        direction = [(0,-1), (0,1), (-1,0), (1, 0)]
        connect = []
        n,m = len(grid), len(grid[0])
        restrictions = {
            # left, right, up, down
            1:[set([1,4,6]), set([1,3,5]),set(),set()],
            2:[set(), set(),set([3,4,2]),set([5,6,2])],
            3:[set([1,4,6]), set(),set(),set([2,5,6])],
            4:[set(), set([1,3,5]),set(),set([2,5,6])],
            5:[set([4,6,1]), set(),set([3,4,2]),set()],
            6:[set(), set([1,3,5]),set([3,4,2]),set()],
        }

        def inbound(i,j):
            return (0 <= i < len(grid) and 0 <= j < len(grid[0]))
        
        queue = deque([(grid[0][0], 0,0)])
        visited = set([(0,0)])

        while queue:
            for _ in range(len(queue)):
                road, row, col = queue.popleft()
                if row == n-1 and col == m-1:
                    return True

                for i in range(4):
                    newrow =row + direction[i][0]
                    newcol =col + direction[i][1]

                    if inbound(newrow, newcol) and (newrow, newcol) not in visited:
                        if grid[newrow][newcol] in restrictions[road][i]:
                            queue.append((grid[newrow][newcol], newrow, newcol))
                            visited.add((newrow, newcol))

        return False