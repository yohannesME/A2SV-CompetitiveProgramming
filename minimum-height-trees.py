class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

            
        adjList = defaultdict(set)
        queue = deque([])
        unvisited = n

        for fromi, toi in edges:
            adjList[fromi].add(toi)
            adjList[toi].add(fromi)
        
        for i in range(n):
            if len(adjList[i]) == 1:
                queue.append(i)
                unvisited -= 1

        while unvisited :
            for _ in range(len(queue)):
                node = queue.popleft()

                parent = adjList[node].pop()

                #remove the node from the parent
                adjList[parent].discard(node)

                #check if the parent becomes a leaf
                if len(adjList[parent]) == 1:
                    queue.append(parent)
                    unvisited -= 1
        return queue