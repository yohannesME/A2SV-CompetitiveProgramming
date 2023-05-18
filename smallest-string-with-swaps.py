class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # parent, size
        n = len(s)
        parent = [i for i in range(n)]
        size = [0]*n

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
        
        for x,y in pairs:
            union(x,y)
        
        ans = list(s)
        reps = defaultdict(list)

        for i in range(n):
            reps[find(i)].append(i)

        for value in reps.values():
            swap = []
            for i in value:
                swap.append(s[i])
            swap.sort()

            for i in range(len(value)):
                ans[value[i]] = swap[i]

        return ''.join(ans)