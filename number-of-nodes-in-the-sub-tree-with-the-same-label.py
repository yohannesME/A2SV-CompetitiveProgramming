class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0]*n
        #make adjacecy list
        adjList = defaultdict(list)

        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        def dfs(node=0):
            #visited
            ans[node] = 1

            #if only one element as neighbour then leaf node
            if len(adjList[node]) == 1 and node:
                return Counter([labels[node]])

            # get all the values of the children and check the count and update the answer
            counter = Counter([labels[node]])
            for child in adjList[node]:
                if not ans[child]:
                    counter += dfs(child)

            ans[node] = counter[labels[node]]
            return counter
        
        dfs()
        return ans