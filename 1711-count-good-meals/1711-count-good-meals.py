class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        #powers of two
        powersOfTwo = [2**i for i in range(22)]
            
        #count of all 
        deliciousCount = Counter()
        
        #answer 
        answer = 0
        
        for d in deliciousness:
            for power in powersOfTwo:
                answer += deliciousCount[power-d]

            
            deliciousCount[d] += 1

    
        
        
        return answer  % ((10**9) + 7)
        

        