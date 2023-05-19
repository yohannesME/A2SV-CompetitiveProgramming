class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Kruskal algorithm 
        # First Union Find
        n = len(points)
        mst = 0
        parent = {}
        size = {}
        
        for point in points:
            parent[tuple(point)] = tuple(point)
            size[tuple(point)] = 1

        def find(member):
            if member == parent[member]:
                return member
            
            parent[member] = find(parent[member])
            return parent[member]
        
        def union(x,y):
            xpar = find(x)
            ypar = find(y)

            if xpar != ypar:
                if size[xpar] > size[ypar]:
                    parent[ypar] = xpar
                    size[xpar] += size[ypar]
                else:
                    parent[xpar] = ypar
                    size[ypar] += size[xpar]
        
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((tuple(points[i]), tuple(points[j]), weight))
        
        edges.sort(key=lambda x: x[2])

        touched = 0
        for edge in edges:
            u,v,w = edge

            if find(u) != find(v):
                union(u,v)
                mst += w
                touched += 1
            
            if touched == n-1:
                break
        return mst