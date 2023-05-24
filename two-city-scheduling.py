class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)

        acount = 0
        bcount = 0
        
        minimum_cost = 0
        n = len(costs)//2

        for acost , bcost in costs:
            if acost < bcost:
                if acount < n:
                    minimum_cost += acost
                    acount += 1
                else:
                    minimum_cost += bcost
                    bcount += 1
            else:
                if bcount < n:
                    minimum_cost += bcost
                    bcount += 1
                else:
                    minimum_cost += acost
                    acount += 1
                
        return minimum_cost