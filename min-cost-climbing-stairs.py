class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        #offset for the starting
        cost.append(0)
        def minClimbing(i,N, memo={}):
            if i >= N:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(minClimbing(i+1, N, memo), minClimbing(i+2,N,memo))
            return memo[i]
        
        return minClimbing(-1, N)