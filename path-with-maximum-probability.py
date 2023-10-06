class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # create distance
        distances = [float('-inf') for _ in range(n)]
        distances[start_node] = 0

        adjList = defaultdict(list)

        for i, (u, v) in enumerate(edges):
            adjList[u].append([v, succProb[i]])
            adjList[v].append([u, succProb[i]])
        

        pq = [(-1, start_node)]
        visited = set()

        while pq:
            curr_distance, node = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)

            for neighbour, cost in adjList[node]:
                distance = -curr_distance * cost
                if distances[neighbour] < distance:
                    distances[neighbour] = distance
                    heapq.heappush(pq, (-distance, neighbour))
        
        return distances[end_node] if distances[end_node] != float('-inf') else 0