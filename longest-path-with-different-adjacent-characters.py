class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        #create an adjacecy list from of a tree from the given path.
        adjList = defaultdict(list)
        N = len(parent)
        #the answer is minimum 1 as we will always have at least one element
        ans = 1

        for i in range(1,N):
            adjList[parent[i]].append(i)
        
        def dfs(node):
            nonlocal ans

            if not adjList[node]:
                return 1
            
            #get the values of each child and exclude those who have the same value as the parent. but also update the ans if we had found the answer
            count = []
            for child in adjList[node]:
                val = dfs(child)
                if s[child] == s[node]:
                    ans = max(ans, val)
                else:
                    count.append(val)
            #if no illigable child then return 1 as the parent is the only one else calculate the maximum
            if not count:
                return 1

            count.sort()
            if len(count) > 1:
                ans = max(ans, count[-1]+count[-2]+1)
            else:
                ans = max(ans, count[-1]+1)
            return count[-1]+1
        dfs(0)

        return ans