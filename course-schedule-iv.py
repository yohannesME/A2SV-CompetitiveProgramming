class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # get the array
        dist = [[False] * numCourses for _ in range(numCourses)]

        for i, j in prerequisites:
            dist[i][j] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):

                    dist[i][j] = dist[i][j] or (dist[i][k] and dist[k][j])
        
        ans = []

        for i,j in queries:
            ans.append(dist[i][j])
        
        return ans