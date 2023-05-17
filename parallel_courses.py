from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
        # Graph as adjacecy list
        adjList = defaultdict(list)
        indegree = [0]*n
        semisters = 0

        for a, b in prerequisites:
            adjList[b-1].append(a-1)
            indegree[a-1] += 1
        
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            semisters += 1
            for _ in range(len(queue)):
                node = queue.popleft()


                for course in adjList[node]:
                    indegree[course] -= 1
                    
                    if indegree[course] == 0:
                        queue.append(course)

        for dep in indegree:
            if dep:
                return -1  

        return semisters
