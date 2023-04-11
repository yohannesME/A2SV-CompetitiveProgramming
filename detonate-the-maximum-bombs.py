class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #create an adjacecy list form the array of bombs
        N = len(bombs)
        adjList = defaultdict(set)
        # visited = set()

        for i in range(N):
            for j in range(i+1, N):
                #if the distance of the center is between the two radius then we can say that they intercept. hence create graph of node connected 
                distance = sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)

                if bombs[i][2] >= distance:
                    adjList[i].add(j)
                if bombs[j][2] >= distance:
                    adjList[j].add(i)

        print(adjList)
        #now the actual work is finding the maximum connected graph length
        def dfs(node, visited):

            if node in visited:
                return 0

            visited.add(node)
            detonate = 1
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    detonate += dfs(neighbour, visited)
            
            return detonate
            
        ans = 0
        for i in range(N):
            ans = max(ans, dfs(i, set()))

        return ans