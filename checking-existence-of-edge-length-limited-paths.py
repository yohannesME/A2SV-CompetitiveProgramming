class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        parent = [x for x in range(n)]
        size = [0]*n

        def find(member):
            if member != parent[member]:
                parent[member] = find(parent[member])
            return parent[member]
        
        def union(u,v):
            upar = find(u)
            vpar = find(v)

            if size[upar] > size[vpar]:
                parent[vpar] = upar
                size[upar] += size[vpar]
            else:
                parent[upar] = vpar
                size[vpar] += size[upar]
        
        edges = defaultdict(list)
        for u, v, d in edgeList:
            edges[d].append((u,v))
        
        qs = defaultdict(list)

        for index , (p,q,l) in enumerate(queries):
            qs[l].append((p,q, index))
        
        ans = [None]*len(queries)
        for x in sorted(set(list(qs.keys()) + list(edges.keys()))):
            if len(qs[x]) > 0:
                for p, q, index in qs[x]:
                    ans[index] = find(p) == find(q)
            
            if len(edges[x]) > 0:
                for u, v in edges[x]:
                    union(u,v)
        
        return ans