class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        values = set()
        visited = set()
        ans = []
        
        for v1, v2 in adjacentPairs:
            values.add(v1)
            values.add(v2)
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        for key in values:
            if len(graph[key]) == 1:
                stack = [key]
                while stack:
                    val = stack.pop()
                    
                    if val not in visited:
                        visited.add(val)
                        ans.append(val)
                        for neighbour in graph[val]:
                            stack.append(neighbour)
                            
                return ans