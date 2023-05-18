class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = []
        inequal = []

        for eq in equations:
            if '==' in eq:
                equal.append(list(map(lambda letter: ord(letter)-97, eq.split('=='))))
            else:
                inequal.append(list(map(lambda letter:ord(letter)-97, eq.split('!='))))

        # parent, size, distance
        n = 26
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
        
        for x,y in equal:
            union(x,y)
        
        for x,y in inequal:
            if isConnected(x,y):
                return False
        return True