class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        package = [0]*k
        self.minUnfairness = float('inf')
        cookies.sort(reverse=True)

        def backtrack(index, package):
            # print(index, package, self.minUnfairness)
            if index == len(cookies):
                self.minUnfairness = min(self.minUnfairness,max(package))
                return
            
            #prunning
            if max(package) >= self.minUnfairness:
                return
            
            # for i in range(index, len(cookies)):
            for j in range(k):
                package[j] += cookies[index]
                backtrack(index+1, package)
                package[j] -= cookies[index]
        
        backtrack(0, package)
        return self.minUnfairness