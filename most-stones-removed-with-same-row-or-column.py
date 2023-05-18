class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # parent, size, distance
        parent = {(a,b):(a,b) for a,b in stones}
        size = {(a,b):1 for a,b in stones}
        

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
                    size[ypar] = 1
                else:
                    parent[xpar] = ypar
                    size[ypar] += size[xpar]
                    size[xpar] = 1
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(tuple(stones[i]), tuple(stones[j]))
        

        ans = 0
        for item in size.values():
            ans += item-1
        return ans