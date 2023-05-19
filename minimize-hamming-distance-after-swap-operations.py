class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # create a union find 
        n = len(source)
        hummingDistance = 0

        parent = [i for i in range(n)]
        size = [0]*n

        def find(member):
            if member == parent[member]:
                return member
            
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
        
        for u,v in allowedSwaps:
            union(u,v)
        
        parentSet = defaultdict(list)

        for i in range(n):
            parentSet[find(i)].append(i)

        #first get a counter of the values
        for swappies in parentSet.values():
            count = Counter(list(map(lambda i: source[i], swappies)))

            for index in swappies:
                if target[index] in count and count[target[index]] != 0:
                    count[target[index]] -= 1
                else:
                    hummingDistance += 1
        
        return hummingDistance