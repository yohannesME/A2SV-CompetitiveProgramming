class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adjList = defaultdict(list)
        ans = []

        for a, b in richer:
            adjList[b].append(a)

        def dfs(node, memo={}):
            if node in memo:
                return memo[node]

            qt = [quiet[node], node]

            for person in adjList[node]:
                qt = min(qt, dfs(person))

            memo[node] = qt
            return qt
        
        for i in range(len(quiet)):
            ans.append(dfs(i)[1])
        return ans