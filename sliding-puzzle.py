class Solution:
    mapping = {
        0:{1,3},
        1:{0,2,4},
        2:{1,5},
        3:{0,4},
        4:{1,3,5},
        5:{2,4},
    }
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        start = []
        for row in board:
            for i in row:
                start.append(str(i))
        
        visited = set(start)
        level = 0
        queue = deque([''.join(start)])

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == '123450':
                    return level
                
                self.addChild(curr, visited, queue)
            level += 1
        return -1
    def addChild(self, curr, visited, queue):
        index = curr.index('0')
        for i in self.mapping[index]:
            s = self.swap(curr, index ,i)
            if s not in visited:
                queue.append(s)
                visited.add(s)
        
    def swap(self, curr, index, i):
        s = list(curr)
        s[index] = s[i]
        s[i] = '0'

        return ''.join(s)