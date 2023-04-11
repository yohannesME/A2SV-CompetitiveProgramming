class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def dfs(i, path):
            if i == n-1:
                return ans.append(path)
            #find all possible path from node
            for neighbour in graph[i]:
                dfs(neighbour, path+[neighbour])

        dfs(0,[0])
        return ans