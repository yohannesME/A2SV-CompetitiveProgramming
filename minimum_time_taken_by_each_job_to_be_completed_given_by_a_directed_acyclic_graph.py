from typing import List


from typing import List
from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        ans = [str(0)]*n
        adjList = defaultdict(list)
        indegree = [0]*n
        queue = deque()
        
        for u,v in edges:
            adjList[u-1].append(v-1)
            indegree[v-1] += 1
            
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        time = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[node] = str(time)
                
                for dep in adjList[node]:
                    indegree[dep] -= 1
                    
                    if indegree[dep] == 0:
                        queue.append(dep)
            time += 1
        return ' '.join(ans)