class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strToDigit(num1)*self.strToDigit(num2))
        
    
    def strToDigit(self,num):
        digits = {}
        for i in range(10):
            digits[str(i)] = i
        
        n1 = digits[num[0]]
        for i in range(1,len(num)):
            n1 = n1*10 + digits[num[i]] 
        return n1