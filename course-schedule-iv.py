class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        ans = []
        indegree = [0]*numCourses

        for v1, v2 in prerequisites:
            adjList[v1].append(v2)
            indegree[v1] += 1
        
        def dfs(node, target, visited):
            visited.add(node)

            if node == target:
                return True

            for child in adjList[node]:
                if child not in visited:
                    if dfs(child, target, visited):
                        return True
            return False
        
        for v1, v2 in queries:
            if indegree[v1] == 0:
                ans.append(False)
            else:
                ans.append(dfs(v1,v2, set()))
        
        return ans