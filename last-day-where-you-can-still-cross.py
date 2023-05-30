class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0, -1)]
        makeIsland = set()
        mst = 0
        parent = {}
        
        for r in range(1,row+1):
            for c in range(1,col+1):
                parent[(r,c)] = (r,c)

        def find(member):
            if member == parent[member]:
                return member
            
            parent[member] = find(parent[member])
            return parent[member]
        
        def union(x,y):
            nonlocal col
            xpar = find(x)
            ypar = find(y)

            if (xpar[0] == 1 and ypar[0] == row) or (xpar[0] == row and ypar[0] == 1):
                return True

            elif (xpar[0] == 1 or xpar[0] == row) and ypar[0] != 1:
                parent[ypar] = xpar
            else:
                parent[xpar] = ypar

            return False

        for i in range(row*col - 1, -1, -1):
            r, c = cells[i]
            for x,y in directions:
                newrow = r + x
                newcol = c + y

                if (newrow , newcol) in makeIsland:
                    if union((newrow, newcol), (r,c)):
                        return i 
            makeIsland.add((r,c))
        return len(cells)