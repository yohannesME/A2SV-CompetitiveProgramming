class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list)

        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visited = set()

        def dfs(node=0):
            visited.add(node)
            if len(adjList[node]) == 1 and node:
                return (2, hasApple[node])
            
            current = 0
            for child in adjList[node]:
                if child not in visited:
                    steps, hasSubApple = dfs(child)
                    if hasSubApple:
                        current += steps

            return (current+2, current or hasApple[node])

        return dfs()[0]-2