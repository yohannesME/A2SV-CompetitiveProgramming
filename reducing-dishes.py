class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        positiveSatisfaction = 0
        posSatisfaction = []
        negSatisfaction = []
        time = 1
        N = len(satisfaction)
        ans = 0

        for i in range(N):
            if satisfaction[i] >= 0:
                posSatisfaction.append(satisfaction[i])
            else:
                negSatisfaction.append(satisfaction[i])
        
        posSatisfaction.sort()
        negSatisfaction.sort(reverse=True)

        for i in range(len(posSatisfaction)):
            if posSatisfaction[i] >= 0:
                ans += time*posSatisfaction[i]
                positiveSatisfaction += posSatisfaction[i]
                time += 1
        
        for i in range(len(negSatisfaction)):
            if negSatisfaction[i] < 0 and -negSatisfaction[i] < positiveSatisfaction:
                positiveSatisfaction += negSatisfaction[i]
                ans += positiveSatisfaction
            else:
                break

        return ans