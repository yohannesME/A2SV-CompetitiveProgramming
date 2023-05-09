class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNode = []
        memo = defaultdict(bool)

        def dfs(node, visited):
            if node in visited:
                return memo[node]
            
            if node in memo:
                return memo[node]
            
            visited.add(node)
            
            if not graph[node]:
                memo[node] = True
                return True
            
            safe = True
            for neighbour in graph[node]:
                safe = dfs(neighbour, visited) and safe
            
            memo[node] = safe
            return safe

        for i in range(len(graph)):
            if dfs(i, set()):
                safeNode.append(i)

        return safeNode