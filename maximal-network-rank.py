class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maximum = 0
        adjacecyList = defaultdict(set)

        for toi, fromi in roads:
            adjacecyList[toi].add(fromi)
            adjacecyList[fromi].add(toi)

        for i in range(n):
            for j in range(i+1, n):
                if j in adjacecyList[i]:
                    maximum = max(maximum, len(adjacecyList[i])+len(adjacecyList[j])-1)
                else:
                    maximum = max(maximum,len(adjacecyList[i])+len(adjacecyList[j]))
        

        return maximum