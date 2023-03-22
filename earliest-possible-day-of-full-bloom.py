class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        #accumulate the plant time and grow time together and create 
        time = []

        for i in range(len(plantTime)):
            time.append([ plantTime[i],growTime[i]])
        time.sort(key=lambda x:(-x[1]))

        accPlant = time[0][0]
        accGrow = time[0][1] + 1
        #ans = gt + max(current-[i][0], [i][1]+1)
        for i in range(len(time)-1):
            accGrow = max(accGrow-time[i+1][0], time[i+1][1]+1)
            accPlant += time[i+1][0]

        return accPlant + accGrow - 1