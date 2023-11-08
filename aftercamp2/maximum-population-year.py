class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Create a list of prefix to hold all the people alive in the 100 year range
        population = [0]*101
        
        #Create the prefix Range
        for start, end in logs:
            population[start-1950] += 1
            population[end - 1950] -= 1
        
        #Iterate and create the answer by adding the values
        answerIndex = 0
        maxLife = population[0]
        for i in range(100):
            population[i+1] += population[i]
            if maxLife < population[i+1]:
                answerIndex = i+1
                maxLife = population[i+1]
        
        return 1950 + answerIndex