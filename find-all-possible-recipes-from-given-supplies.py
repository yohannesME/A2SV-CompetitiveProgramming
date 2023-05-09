class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        supplies =set(supplies)
        N = len(recipes)
        indegree = defaultdict(int)
        adjList = defaultdict(list)
        orderedrecipe = []
        

        for i in range(N):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplies:
                    adjList[ingredients[i][j]].append(recipes[i])
                    indegree[recipes[i]] += 1
        
        queue = deque()

        for i in range(N):
            if indegree[recipes[i]] == 0:
                queue.append(recipes[i])
        
        while queue:
            for _ in range(len(queue)):
                recipe = queue.popleft()
                orderedrecipe.append(recipe)

                for otherrecipe in adjList[recipe]:
                    indegree[otherrecipe] -= 1

                    if indegree[otherrecipe] == 0:
                        queue.append(otherrecipe)
        
        return orderedrecipe