class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # #create an array of adjacency list to find the one nodes that are not traversed
        # adjacentList = defaultdict(set)
        # #assume that we can not reach any node
        # ans = set([i for i in range(n)])

        # #create the adjacecy list from the edges
        # for fromi, toi in edges:
        #     adjacentList[fromi].add(toi)
        
        # #remove the nodes that we can reach
        # for i in range(n):
        #     ans -= adjacentList[i]
        
        # return list(ans)
        #the answer
        ans = []
        #create a list of keep track of occurances
        reachable = [0 for _ in range(n)]

        for fromi, toi in edges:
            reachable[toi] += 1
        
        for i in range(n):
            #if we can't reach that node then we must append it
            if reachable[i] == 0:
                ans.append(i)
        
        return ans