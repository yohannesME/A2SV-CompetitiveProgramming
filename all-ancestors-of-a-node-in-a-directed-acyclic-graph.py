class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [[] for _ in range(n)]
        adjList = defaultdict(list)

        for fromi, toi in edges:
            adjList[fromi].append(toi)

        def dfs(node,ancestor, visited):
            for child in adjList[node]:
                if child not in visited:
                    ancestors[child].append(ancestor)
                    visited.add(child)
                    dfs(child, ancestor, visited)
        
        for i in range(n):
            dfs(i, i, set())
                
        return ancestors