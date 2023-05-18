class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # parent, size, distance
        parent = [i for i in range(n)]
        size = [0]*n
        distance = [float('inf')]*n

        def find(member):
            if member == parent[member]:
                return member
            
            parent[member] = find(parent[member])
            return parent[member]
        
        def union(x,y, d):
            xpar = find(x)
            ypar = find(y)

            if size[xpar] > size[ypar]:
                parent[ypar] = xpar
                distance[xpar] = min(distance[xpar], distance[ypar], d)
                size[xpar] += size[ypar]
            else:
                parent[xpar] = ypar
                distance[ypar] = min(distance[xpar], distance[ypar], d)
                size[ypar] += size[xpar]
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        for x,y, d in roads:
            union(x-1,y-1,d)
        
        return distance[find(0)]