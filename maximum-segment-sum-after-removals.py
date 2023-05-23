class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        #union find with out path compression and also size
        n = len(nums)
        prefix = [0]
        parent = [i for i in range(n)]
        maximum = 0
        ans = [0]
        max_values = nums[:]
        size = [1]*n
        allowed = set()

        for num in nums:
            prefix.append(prefix[-1]+ num)

        def find(member):
            if member == parent[member]:
                return member
            return find(parent[member])
        
        def union(x,y):
            nonlocal maximum
            xpar = find(x)
            ypar = find(y)

            if xpar != ypar:
                if size[xpar] > size[ypar]:
                    parent[ypar] = xpar
                    size[xpar] += size[ypar]
                    max_values[xpar] += max_values[ypar]
                    maximum = max(maximum, max_values[xpar])
                else:
                    parent[xpar] = ypar
                    size[ypar] += size[xpar]
                    max_values[ypar] += max_values[xpar]
                    maximum = max(maximum, max_values[ypar])


        
        for i in range(len(removeQueries)-1,0,-1):
            if removeQueries[i]+1 in allowed:
                union(removeQueries[i]+1, removeQueries[i])
            if removeQueries[i]-1 in allowed:
                union(removeQueries[i]-1, removeQueries[i])
                
            allowed.add(removeQueries[i])
            maximum = max(maximum, nums[removeQueries[i]])
            ans.append(maximum)

        return reversed(ans)