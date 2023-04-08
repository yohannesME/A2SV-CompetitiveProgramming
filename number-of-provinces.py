class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #keep track of the visited and also the componens
        visited = set()
        ans = 0
        n = len(isConnected)

        #use dfs to traverse as much as possible to check each sub routes
        def dfs(node):
            for neighbour in range(n):
                if isConnected[node][neighbour] and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
        
        #if there are disconnected conmponenets count each and update our answer and traverse each one
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        
        return ans