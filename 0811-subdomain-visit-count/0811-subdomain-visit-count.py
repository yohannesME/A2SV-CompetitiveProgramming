class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visitCount = {}
        
        for cpdomain in cpdomains:
            count, domains = cpdomain.split(' ')
            count = int(count)
            

            while len(domains) > 0:
                
                if domains in visitCount:
                    visitCount[domains] += count
                else:
                    visitCount[domains] = count
                
                index = domains.find('.')
                if index != -1:
                    domains = domains[index+1:]
                else:
                    domains = ''
            
        print(visitCount)
        
        answer = []
        
        for key, values in visitCount.items():
            answer.append(str(values) +' '+ key)
            
        return answer
        