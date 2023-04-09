class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        #create a adjacecy list for a dfs
        adjList = defaultdict(list)
        #one for the offset initialize our colors
        colors = [-1]*(n+1)
        visited = set()

        for v1, v2 in dislikes:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        def dfs(node, color):
            #if node visited before let's check if it's color is a match with the revisit
            if node in visited:
                return colors[node] == color
            
            visited.add(node)

            #if not visited and already has the intended color then no bipartition possible
            if colors[node] == color:
                return False
            
            #if then color and color the adjacent list with different color
            colors[node] = color
            for adj in adjList[node]:
                if not dfs(adj, color^1):
                    return False
            return True
        
        #as the graph may be disconnected we traverse each one to check all
        for i in range(1,n+1):
            if i not in visited:
                if not dfs(i, 0):
                    return False
        #if one value had returned false we would return False if not we made sure so return True
        return True