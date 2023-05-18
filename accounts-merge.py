class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # parent, size, distance
        parent = {}
        size = {}
        parentName = {}

        def find(member):
            if member not in parent:
                parent[member] = member
                size[member] = 1
                return member

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
        
        for account in accounts:
            parentName[account[1]] = account[0]
            if account[1] not in parent:
                parent[account[1]] = account[1]
                size[account[1]] = 1

            for i in range(2, len(account)):
                parentName[account[i]] = account[0]
                union(account[1], account[i])

        representers = defaultdict(list)
        for key,value in parent.items():
            representers[find(value)].append(key)
        
        ans = []

        for key,value in representers.items():
            value.sort()
            ans.append([parentName[key]]+value)
        return ans