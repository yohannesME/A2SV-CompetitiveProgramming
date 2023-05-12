from collections import defaultdict
import string

class Solution:
    def findOrder(self,alien_dict, N, K):
        adjList = defaultdict(set)
        ans = []
        for i in range(N):
            for j in range(i+1, N):
                ptr1 = 0
                found = False
                while ptr1 < len(alien_dict[i]) and ptr1 < len(alien_dict[j]):
                    if alien_dict[i][ptr1] != alien_dict[j][ptr1]:
                        if alien_dict[i][ptr1] not in adjList[alien_dict[j][ptr1]]:
                            adjList[alien_dict[j][ptr1]].add(alien_dict[i][ptr1])
                        found = True
                        break
                    ptr1 += 1
                if found:
                    break
        
        def dfs(node, visited=set()):
            if node in visited:
                return
            visited.add(node)
            for child in adjList[node]:
                dfs(child, visited)
            
            ans.append(node)
        
        for letter in string.ascii_lowercase[:K]:
            dfs(letter)
            
        return ans