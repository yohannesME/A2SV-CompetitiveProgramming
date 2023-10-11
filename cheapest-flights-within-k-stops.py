class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        adjList = defaultdict(list)
        for u, v, w in flights:
            adjList[u].append((v,w))
        
        heap = [(0, k ,  src)]
        visited = set()

        while heap:
            w, k , node = heappop(heap)

            if (node, k) in visited:
                continue
            
            visited.add((node, k))

            if k < -1:
                continue

            if k == -1 and node == dst:
                return w
            

            if node == dst:
                return w


            for neighbour, nw in adjList[node]:
                heappush(heap, (w + nw, k-1, neighbour))

        return -1