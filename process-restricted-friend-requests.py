class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        adjList = defaultdict(set)
        for u,v in restrictions:
            adjList[u].add(v)
            adjList[v].add(u)
        

        parent = [i for i in range(n)]
        size = [0]*n
        members = [set([i]) for i in range(n)]

        def find(member):
            if member == parent[member]:
                return member
            
            parent[member] = find(parent[member])
            return parent[member]
        
        def union(x,y):
            xpar = find(x)
            ypar = find(y)

            if xpar != ypar:
                restrict = set()
                for val in members[xpar]:
                    restrict.update(adjList[val])

                if restrict.intersection(members[ypar]):
                    return False

                if size[xpar] > size[ypar]:
                    parent[ypar] = xpar
                    size[xpar] += size[ypar]
                    members[xpar].update(members[ypar])
                else:
                    parent[xpar] = ypar
                    size[ypar] += size[xpar]
                    members[ypar].update(members[xpar])
            return True
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        ans = []
        for a,b in requests:
            ans.append(union(a,b))
        
        return ans