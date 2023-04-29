class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        answer = [[0]*len(mat[0]) for i in range(len(mat))]
        visited = [[False]*len(mat[0]) for i in range(len(mat))]
        queue = deque()

        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))


        def bfs():
            distance = 1
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    for row_change, col_change in directions:
                        new_row = row + row_change
                        new_col = col + col_change
            
                        if inbound(new_row, new_col) and not visited[new_row][new_col]:
                            if mat[new_row][new_col]:
                                answer[new_row][new_col] = distance
                                queue.append((new_row, new_col))
                                visited[new_row][new_col] = True
                distance += 1
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if not mat[r][c]:
                    queue.append((r,c))
        
        bfs()

        return answer