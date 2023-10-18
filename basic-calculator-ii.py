class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        current = prev = 0
        
        operation = '+'
        
        i = 0
        
        while i < len(s):
            
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    current = current*10 + int(s[i])
                    
                    i+=1
                i -= 1
                
                if operation == "+":
                    result += current
                    
                    prev = current
                elif operation == "-":
                    result -= current
                    
                    prev = -current
                elif operation == "*":
                    result -= prev
                    result += prev*current
                    
                    prev = current * prev
                else:
                    result -= prev
                    result += int(prev/current)
                    
                    prev = int(prev/current)
                
                current = 0
            elif s[i] != " ":
                operation = s[i]
            
            i += 1
        return result