class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        sN = len(strs[0])
        parent = [i for i in range(N)]
        size = [1]*N

        def find(x):
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(u,v):
            up = find(u)
            vp = find(v)

            if size[up] > size[vp]:
                parent[vp] = up
                size[up] += size[vp]
            else:
                parent[up] = vp
                size[vp] += size[up]
        
        def isConnected(u,v):
            return find(u) == find(v)
        
        for i in range(N):
            for j in range(i+1, N):
                
                if find(i) == find(j):
                    continue

                diff = 0
                for x in range(sN):
                    diff += (strs[i][x] != strs[j][x])
                if diff <= 2:
                    union(i,j)
        ans = set()
        for i in range(N):
            ans.add(find(i))
        return len(ans)