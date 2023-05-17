class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        size = [0]*n
        # let's create a union find 
        def find(member):
            if member == parent[member]:
                return member
            
            parent[member] = find(parent[member])
            return parent[member]
        
        def union(x,y):
            xpar = find(x)
            ypar = find(y)

            if size[xpar] > size[ypar]:
                parent[ypar] = xpar
                size[xpar] += size[ypar]
            else:
                parent[xpar] = ypar
                size[ypar] += size[xpar]
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        for x,y in edges:
            union(x,y)
        
        return isConnected(source, destination)