class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # parent, size, distance
        parent = [i for i in range(26)]
        size = [0]*26
        smallest = [i for i in range(26)]

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
                smallest[xpar] = min(smallest[xpar], smallest[ypar])
                size[xpar] += size[ypar]
            else:
                parent[xpar] = ypar
                smallest[ypar] = min(smallest[xpar], smallest[ypar])
                size[ypar] += size[xpar]
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        for i in range(len(s1)):
            union(ord(s1[i])-97, ord(s2[i])-97)
        
        ans = []

        for letter in baseStr:
            val = find(ord(letter)-97)
            ans.append(chr(smallest[val]+97))
        
        return ''.join(ans)