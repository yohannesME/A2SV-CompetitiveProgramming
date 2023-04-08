class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #create a adjacecy list from the adjacecy matrix
        adjList = defaultdict(set)
        n = len(isConnected)

        for i in range(n):
            for j in range(i,n):
                if isConnected[i][j]:
                    adjList[i].add(j)
                    adjList[j].add(i)

        #keep track of the visited and also the componens
        visited = set()
        ans = 0

        #use dfs to traverse as much as possible to check each sub routes
        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for val in adjList[node]:
                dfs(val)
        
        #if there are disconnected conmponenets count each and update our answer and traverse each one
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        
        return ans