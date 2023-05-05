from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #tag the label
        labels = {}
        reverse = False
        n = len(board)
        tag = 1
        for row in range(n-1, -1,-1):
            if reverse:
                for col in range(n-1,-1,-1):
                    labels[tag] = (row,col)
                    tag += 1
            else:
                for col in range(n):
                    labels[tag] = (row,col)
                    tag += 1
            
            reverse = not reverse
        
        visited = set([(1, n-1,0)])
        ladderVisited = set()
        queue = deque([(1, n-1, 0)])

        distance = 0

        while queue:
            print(queue,visited)
            for _ in range(len(queue)):
                current_tag, row, col = queue.popleft()
                
                if current_tag == n*n:
                    return distance

                for i in range(current_tag + 1, min(current_tag+6, len(labels)) + 1):
                    next_row, next_col = labels[i]

                    if (next_row, next_col) in visited:
                        continue

                    if board[next_row][next_col] == -1:
                        visited.add((next_row, next_col))
                        queue.append((i, next_row, next_col))
                    else:
                        snakeLadder = board[next_row][next_col]
                        if labels[snakeLadder] in ladderVisited:
                            continue

                        if labels[snakeLadder] not in visited:
                            ladderVisited.add(labels[snakeLadder])
                            queue.append((snakeLadder, labels[snakeLadder][0], labels[snakeLadder][1]))

            distance += 1
        
        return -1