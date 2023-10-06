class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        variables = set()

        for i, (u,v) in enumerate(equations):
            variables.add(u)
            variables.add(v)
            # graph[u].append([v,values[i]])
            # graph[v].append([u,1/values[i]])
        
        n = len(variables)
        dist = [[float('inf')]*n for _ in range(n)]
        
        index = {}
        idx = 0
        for val in variables:
            index[val] = idx
            idx += 1
        
        for i in range(n):
            dist[i][i] = 1

        for i, (u, v) in enumerate(equations):
            dist[index[u]][index[v]] = values[i]
            dist[index[v]][index[u]] = 1/values[i]
        
        for k in range(n):
             for i in range(n):
                  for j in range(n):
                      dist[i][j] = min(dist[i][j] , dist[i][k] * dist[k][j])

        ans = []

        for u, v in queries:
            if u not in variables or v not in variables:
                ans.append(-1.0)
                continue
                
            val = dist[index[u]][index[v]]
            ans.append(val if val != float('inf') else -1)
        
        return ans