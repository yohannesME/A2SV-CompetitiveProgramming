class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        answer = [[0]*k for _ in range(k)]

        def topoSort(condition):
            adjList = defaultdict(list)
            indegree = [0]*k

            for a, b in condition:
                adjList[a].append(b)
                indegree[b-1] += 1

            queue = deque()

            for i, val in enumerate(indegree):
                if val == 0:
                    queue.append(i + 1)
            
            ordered = []

            while queue:
                node = queue.popleft()
                ordered.append(node)

                for child in adjList[node]:
                    indegree[child - 1] -= 1

                    if indegree[child -1] == 0:
                        queue.append(child)
            
            return ordered

        row_order = topoSort(rowConditions)
        col_order = topoSort(colConditions)

        if len(row_order) < k or len(col_order) < k:
            return []

        col_order_map = {}
        for i , order in enumerate(col_order):
            col_order_map[order] = i

        for row, val in enumerate(row_order):
            answer[row][col_order_map[val]] = val
        
        return answer