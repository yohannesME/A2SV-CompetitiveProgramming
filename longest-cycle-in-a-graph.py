class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # create a adjacecylist
        adjList = defaultdict(list)
        for i in range(len(edges)):
            adjList[edges[i]].append(i)

        #dfs function iterate through each node and check to find a cycle and exclude if any for any future call
        def dfs(start, node, visited, cycle=set()):
            if node == -1 or node in cycle:
                return float('-inf')
            if node in visited:
                if node == start:
                    cycle.update(visited)
                    return 0
                else:
                    return float('-inf')
            visited.add(node)
            return 1 + dfs(start,edges[node], visited , cycle)
        
        ans = -1
        for i in range(len(edges)):
            ans = max(ans, dfs(i, i, set()))
        return ans