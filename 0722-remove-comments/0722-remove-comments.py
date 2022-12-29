class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        #the answer 
        answer = []
        
        #check if in a multi line comment
        inComment = False
        
        #new with out comment produced string
        uncommented = ""
        
        for line in source:
            if not inComment:
                uncommented = ""
            left = 0 
            n = len(line)
            
            # inComment, we find */
            while left < n:
                if inComment:
                    if line[left:left + 2] == '*/' and left + 1 < n:
                        left += 2
                        inComment = False
                        continue
                    left += 1
                    
                # not in Comment, we find /* // and common character
                else:
                    if line[left:left + 2] == '/*' and left + 1 < n:
                        left += 2
                        inComment = True
                        continue
                        
                    if line[left:left + 2] == '//' and left + 1 < n:
                        break
                    uncommented += line[left]
                    left += 1
                    
            if uncommented and not inComment:
                answer.append(uncommented)
                    

        return answer