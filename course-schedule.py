class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph as adjacecy list
        adjList = defaultdict(list)
        indegree = [0]*numCourses

        for a, b in prerequisites:
            adjList[b].append(a)
            indegree[a] += 1
        
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()


                for course in adjList[node]:
                    indegree[course] -= 1
                    
                    if indegree[course] == 0:
                        queue.append(course)

        for dep in indegree:
            if dep:
                return False

        return True